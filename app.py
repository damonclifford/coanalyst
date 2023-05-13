from flask import Flask, request, render_template
from sqlalchemy import create_engine, text
import openai
import pandas as pd
import config

app = Flask(__name__)
openai.api_key = config.OPENAI_API_KEY
df = pd.read_csv('assets/Online_Retail_1000_v2.csv')
# Calculate total sales and add as a new column
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

def create_table_definition(df):
    prompt = '''### sqlite SQL table, with its properties:
    #
    # Data({})
    #
    '''.format(','.join(str(col) for col in df.columns))

    return prompt

def combine_prompts(df, query_prompt):
    definition = create_table_definition(df)
    query_init_string = f'### A query to answer: {query_prompt}\nSELECT'
    return definition + query_init_string

def generate_sql_and_response(nlp_text):
    # Create temporary in-memory SQLite database and push Pandas dataframe to it
    temp_db = create_engine('sqlite:///:memory:', echo=True)
    data = df.to_sql(name='Data', con=temp_db)

    # Combine NLP input, dataframe, and SQL query
    combined_prompt = combine_prompts(df, nlp_text)

    # Call OpenAI API to generate SQL query from combined prompt
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=combined_prompt,
        temperature=0.1,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=['#',';']
    )

    # Extract SQL query from OpenAI API response
    query = response['choices'][0]['text']

    # Add SELECT statement if not present in SQL query
    if query.startswith(' '):
        query = 'SELECT'+query

    # Execute SQL query on temporary database and save output
    with temp_db.connect() as conn:
        result = conn.execute(text(query))
        output = result.all()

    # Call OpenAI API to generate natural language response from NLP text and SQL query output
    user_response = openai.Completion.create(
        model='text-davinci-003',
        prompt=nlp_text + ' ' + str(output),
        temperature=0.1,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=['SENTENCE']
    )

    # Extract natural language response from OpenAI API response
    response = user_response['choices'][0]['text']

    return query, output, response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Prompt user for NLP input
        nlp_text = request.form['question']

        # Generate SQL and natural language response
        query, output, response = generate_sql_and_response(nlp_text)

        # Return the question, SQL query, and natural language response as strings
        return render_template('index.html', question=nlp_text, query=query, output=output, response=response)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
