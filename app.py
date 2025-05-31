from flask import Flask, request, render_template
from sqlalchemy import create_engine, text
import pandas as pd
import config
import re

app = Flask(__name__)

# Try to import the new OpenAI client, fallback to old version
try:
    from openai import OpenAI
    # New API (v1.0+)
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    USE_NEW_API = True
except ImportError:
    # Old API (pre-v1.0)
    import openai
    openai.api_key = config.OPENAI_API_KEY
    USE_NEW_API = False

df = pd.read_csv('assets/Online_Retail_1000_v2.csv')
# Calculate total sales and add as a new column
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

def create_table_definition(df):
    prompt = '''### sqlite SQL table, with its properties:
    #
    # Sales({})
    #
    '''.format(','.join(str(col) for col in df.columns))
    return prompt

def combine_prompts(df, query_prompt):
    definition = create_table_definition(df)
    query_init_string = f'### A query to answer: {query_prompt}\nSELECT'
    return definition + query_init_string

def clean_sql_query(query):
    """Clean and validate the SQL query"""
    # Remove leading/trailing whitespace
    query = query.strip()

    # Add SELECT if missing
    if not query.upper().startswith('SELECT'):
        query = 'SELECT ' + query

    # Remove comments and clean up the query
    query = re.sub(r'--.*$', '', query, flags=re.MULTILINE)
    query = re.sub(r'/\*.*?\*/', '', query, flags=re.DOTALL)

    # Remove extra whitespace
    query = ' '.join(query.split())

    # Ensure query ends properly (remove trailing semicolons if present)
    query = query.rstrip(';')

    return query

def call_openai_completion(prompt, max_tokens=150, stop=None):
    """Call OpenAI API with compatibility for both old and new versions"""
    try:
        if USE_NEW_API:
            # New API (v1.0+)
            response = client.completions.create(
                model='gpt-3.5-turbo-instruct',
                prompt=prompt,
                temperature=0.1,
                max_tokens=max_tokens,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=stop
            )
            return response.choices[0].text.strip()
        else:
            # Old API (pre-v1.0) - use available models
            try:
                # Try gpt-3.5-turbo-instruct first
                response = openai.Completion.create(
                    model='gpt-3.5-turbo-instruct',
                    prompt=prompt,
                    temperature=0.1,
                    max_tokens=max_tokens,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                    stop=stop
                )
                return response['choices'][0]['text'].strip()
            except:
                # Fallback to text-davinci-002 if available
                try:
                    response = openai.Completion.create(
                        model='text-davinci-002',
                        prompt=prompt,
                        temperature=0.1,
                        max_tokens=max_tokens,
                        top_p=1.0,
                        frequency_penalty=0.0,
                        presence_penalty=0.0,
                        stop=stop
                    )
                    return response['choices'][0]['text'].strip()
                except:
                    # If all else fails, return a simple response
                    return "Unable to generate response due to API limitations."
    except Exception as e:
        print(f"OpenAI API Error: {str(e)}")
        return f"Error calling OpenAI API: {str(e)}"

def generate_sql_and_response(nlp_text):
    try:
        # Create temporary in-memory SQLite database and push Pandas dataframe to it
        temp_db = create_engine('sqlite:///:memory:', echo=False)
        df.to_sql(name='Sales', con=temp_db, if_exists='replace', index=False)

        # Combine NLP input, dataframe, and SQL query
        combined_prompt = combine_prompts(df, nlp_text)

        # Call OpenAI API to generate SQL query
        query_response = call_openai_completion(
            combined_prompt,
            max_tokens=150,
            stop=['#', ';']
        )

        # Extract and clean SQL query
        query = clean_sql_query(query_response)

        print(f"Generated SQL: {query}")  # For debugging

        # Execute SQL query on temporary database and save output
        try:
            with temp_db.connect() as conn:
                result = conn.execute(text(query))
                output = result.fetchall()
        except Exception as sql_error:
            print(f"SQL Error: {str(sql_error)}")
            # Return a simple fallback query
            query = "SELECT COUNT(*) FROM Sales"
            with temp_db.connect() as conn:
                result = conn.execute(text(query))
                output = result.fetchall()

        # Create a more natural language prompt for the response
        response_prompt = f"""
        Question: {nlp_text}
        SQL Query Result: {output}

        Please provide a natural language response explaining the results in a helpful way.
        """

        # Call OpenAI API to generate natural language response
        response_text = call_openai_completion(response_prompt, max_tokens=150)

        return query, output, response_text

    except Exception as e:
        print(f"Error in generate_sql_and_response: {str(e)}")
        error_query = f"-- Error generating query for: {nlp_text}"
        error_output = []
        error_response = f"Sorry, I encountered an error processing your request: {str(e)}"
        return error_query, error_output, error_response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get user input
            nlp_text = request.form.get('question', '').strip()

            if not nlp_text:
                return render_template('index.html',
                                     error="Please enter a question.")

            # Generate SQL and natural language response
            query, output, response = generate_sql_and_response(nlp_text)

            # Return the question, SQL query, and natural language response as strings
            return render_template('index.html',
                                 question=nlp_text,
                                 query=query,
                                 output=output,
                                 response=response)

        except Exception as e:
            print(f"Error in index route: {str(e)}")
            return render_template('index.html',
                                 error=f"An error occurred: {str(e)}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

</body>
</html>
