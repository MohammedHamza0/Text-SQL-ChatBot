import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv(override=True)
import sqlite3

from src.config.config import SAFETY_SETTINGS, GENERATION_CONFIG



# Load environment variables from .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# Configuring the API key for Google Generative AI
genai.configure(api_key=GEMINI_API_KEY)



def create_sql_code(question, prompt, model = "gemini-2.5-flash-preview-04-17"):

    model = genai.GenerativeModel(model_name=model,
                                  generation_config=GENERATION_CONFIG,
                                  safety_settings=SAFETY_SETTINGS)

    # Prompt template
    prompt_template = f"""
    {prompt}
    Question: {question}
    """

    # Generate content
    response = model.generate_content(prompt_template)

    # Extract the generated SQL code
    generated_sql_code = response.text

    return generated_sql_code



# function to retrive query from the database
def query_database(query, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

