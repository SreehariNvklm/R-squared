import streamlit as st
from src.database.db_query import DB_Query
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

st.set_page_config(page_title="Verdict Chat",page_icon=":speech_balloon:")

def response_generation(user_query,case_file):
    history = []
    genai.configure(os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"Given the retrieved case file according to the user query: {user_query}, case file: {case_file}"
    response = model.generate_content(prompt,history)
    return response.text