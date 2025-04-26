

# LLM configuration for SQL query generation
LLM_PROMPT = """    You are an advanced SQL query generator.
                    Given a user's natural language question, convert it into a syntactically correct and efficient SQL query based on the following database schema:

                    Table: students

                    Columns:
                    name (VARCHAR)
                    age (INTEGER)
                    grade (VARCHAR)
                    
                    Instructions:
                    Focus strictly on generating SQL code only.
                    Do not add any explanations, formatting, or extra text.
                    Assume the user input is simple and relates only to the provided table and columns.
                    Be case-insensitive to the user input.
                    Always wrap string values (like names or grades) in single quotes.
                    Output only the SQL query.
                    Do not include any comments or additional text."""
          

# generation configuration for the LLM
GENERATION_CONFIG = {
     "temperature": 0.4,
     "top_p": 1,
     "top_k": 32,
     "max_output_tokens": 2048,
}

# Safety settings to block harmful content
SAFETY_SETTINGS = [
     {
          "category": "HARM_CATEGORY_HARASSMENT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
     {
          "category": "HARM_CATEGORY_HATE_SPEECH",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
     {
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
     {
          "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
     }
]
          
          
