import os
import re

from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
import pandas as pd

import config

app = Flask(__name__)

# Modern OpenAI client configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or getattr(config, "OPENAI_API_KEY", "")

try:
    from openai import OpenAI

    client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY and OPENAI_API_KEY != "YOUR-OPENAI-API-KEY" else None
except ImportError:
    client = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "assets", "Online_Retail_1000_v2.csv")

# Load the dataset from a stable app-relative path
try:
    df = pd.read_csv(CSV_PATH)
except FileNotFoundError:
    df = pd.read_csv(os.path.join(BASE_DIR, "data", "Online_Retail_1000_v2.csv"))

# Calculate total sales and add as a new column
if "TotalSales" not in df.columns:
    df["TotalSales"] = df["Quantity"] * df["UnitPrice"]


def create_table_definition(df):
    columns = ", ".join(str(col) for col in df.columns)
    return (
        "You are generating valid SQLite SQL for a sales dataset. "
        f"Table name: Sales. Columns: {columns}. "
        "Return ONLY the SQL statement with no markdown fences, no explanation, "
        "and no extra commentary."
    )


def combine_prompts(df, query_prompt):
    definition = create_table_definition(df)
    return (
        f"{definition}\n\n"
        "Use the columns exactly as provided. "
        "Do not invent columns. "
        "Do not use unsupported SQLite functions. "
        "Ignore nulls where appropriate.\n\n"
        f"Question: {query_prompt}\n\n"
        "SQL:"
    )


def clean_sql_query(query):
    """Clean and normalize a SQL query returned by the model."""
    if not query:
        return "SELECT COUNT(*) FROM Sales"

    # Strip markdown fences if the model returns them
    query = query.strip()
    query = re.sub(r"^```(?:sql)?\s*", "", query, flags=re.IGNORECASE)
    query = re.sub(r"\s*```$", "", query, flags=re.IGNORECASE)

    # Extract the first SQL statement if the model includes surrounding text
    match = re.search(r"SELECT\b.*", query, flags=re.IGNORECASE | re.DOTALL)
    if match:
        query = match.group(0)

    # Ensure it is a SELECT statement
    if not re.match(r"^SELECT\b", query, flags=re.IGNORECASE):
        query = "SELECT " + query.lstrip()

    # Remove trailing semicolons and extra whitespace
    query = query.rstrip(";")
    query = " ".join(query.split())
    return query


def call_openai_completion(prompt, max_tokens=300, temperature=0.1):
    """Call the modern OpenAI chat completions API."""
    if client is None:
        return "OpenAI API key is not configured. Set OPENAI_API_KEY in your environment or config.py."

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a careful SQL generation assistant for SQLite. "
                        "Return only valid SQL without markdown fences or explanations."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()
    except Exception as exc:
        print(f"OpenAI API Error: {exc}")
        return f"Error calling OpenAI API: {exc}"


def generate_sql_and_response(nlp_text):
    try:
        temp_db = create_engine("sqlite:///:memory:", echo=False)
        df.to_sql(name="Sales", con=temp_db, if_exists="replace", index=False)

        combined_prompt = combine_prompts(df, nlp_text)
        query_response = call_openai_completion(
            combined_prompt,
            max_tokens=250,
            temperature=0.1,
        )

        if query_response.startswith("Error calling OpenAI API") or "not configured" in query_response:
            return "SELECT COUNT(*) FROM Sales", [], query_response

        query = clean_sql_query(query_response)
        print(f"Generated SQL: {query}")

        try:
            with temp_db.connect() as conn:
                result = conn.execute(text(query))
                rows = result.fetchall()
                columns = result.keys()
                output = [dict(zip(columns, row)) for row in rows]
        except Exception as sql_error:
            print(f"SQL Error: {sql_error}")
            query = "SELECT COUNT(*) FROM Sales"
            with temp_db.connect() as conn:
                result = conn.execute(text(query))
                rows = result.fetchall()
                columns = result.keys()
                output = [dict(zip(columns, row)) for row in rows]

        response_prompt = (
            "You are a helpful data analyst. Respond in plain English, using the data below.\n\n"
            f"Question: {nlp_text}\n"
            f"SQL Query: {query}\n"
            f"Result: {output}\n\n"
            "Write a concise and informative answer that explains the result clearly."
        )

        response_text = call_openai_completion(response_prompt, max_tokens=250, temperature=0.2)

        if response_text.startswith("Error calling OpenAI API") or "not configured" in response_text:
            response_text = "I generated a query and retrieved the results, but the response model is unavailable right now."

        return query, output, response_text

    except Exception as exc:
        print(f"Error in generate_sql_and_response: {exc}")
        return (
            "SELECT COUNT(*) FROM Sales",
            [],
            f"Sorry, I encountered an error processing your request: {exc}",
        )


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            nlp_text = request.form.get("question", "").strip()

            if not nlp_text:
                return render_template("index.html", error="Please enter a question.")

            query, output, response = generate_sql_and_response(nlp_text)

            return render_template(
                "index.html",
                question=nlp_text,
                query=query,
                output=output,
                response=response,
            )

        except Exception as exc:
            print(f"Error in index route: {exc}")
            return render_template("index.html", error=f"An error occurred: {exc}")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
