import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv(override=True)   
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
from src.config.config import LLM_PROMPT
from src.helpers import create_sql_code, query_database



def main():
     st.set_page_config(page_title="SQL Query Generator", page_icon=":robot_face:")
     st.title("SQL Query Generator")
     st.info("This app generates SQL queries based on user input.")

     # Initialize session state variables
     if "generated_sql_code" not in st.session_state:
               st.session_state.generated_sql_code = None
     if "query_results" not in st.session_state:
               st.session_state.query_results = None

     with st.sidebar:
          st.header("GEMINI API Key")
          api_key = st.text_input("Enter your GEMINI API Key", type="password", key="api_key")
          st.markdown("[Get your GEMINI API Key](https://aistudio.google.com/apikey)")

          if api_key == GEMINI_API_KEY:
               st.success("API Key entered successfully!")
               
          if (api_key != GEMINI_API_KEY) and (api_key != ""):
               st.error("Invalid API Key. Please check your API Key and try again.")
               
          if api_key == "":
               st.warning("Please enter your API Key to continue.")
               st.stop()

          st.markdown("---")
          st.header("Instructions")
          st.write("1. Enter your question in the text box.")
          st.write("2. Click the 'Generate SQL Query' button.")
          st.write("3. The generated SQL query will be displayed below.")
          st.write("4. You can also run the generated SQL query on the database.")
          st.write("5. Make sure to have a SQLite database file ready for querying.")
          st.write("6. Enjoy!")

     question = st.text_input("Enter your question", key="question")
     if st.button("Generate SQL Query"):
               if api_key == GEMINI_API_KEY:
                    with st.spinner("Generating SQL Query..."):
                         generated_sql_code = create_sql_code(question, LLM_PROMPT)
                         st.session_state.generated_sql_code = generated_sql_code
                         st.session_state.query_results = None  # Reset query results when a new query is generated

     if st.session_state.generated_sql_code:
               st.caption("SQL Query generated successfully!")      
               st.code(st.session_state.generated_sql_code)
               if st.button("Run Query"):
                    with st.spinner("Running Query..."):
                         cleaned_query = st.session_state.generated_sql_code.strip("`").replace("sql", "").strip()
                         results = query_database(cleaned_query, "database/students.db")
                         st.session_state.query_results = results

                    # Display query results if available
                    if st.session_state.query_results:
                              st.success("Query executed successfully!") 
                              st.markdown("### Query Results") 
                              st.dataframe(st.session_state.query_results, use_container_width=True, on_select="rerun")
                              # st.write(st.session_state.query_results)
                    else:
                              st.warning("No results to display.")


if __name__ == "__main__":
    main()
