import streamlit as st
from src.database.db_query import DB_Query
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

st.set_page_config(page_title="Verdict Chat", page_icon=":speech_balloon:")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_model" not in st.session_state:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash")
    st.session_state.chat_model = model.start_chat(history=[])

query_obj = DB_Query()

def response_generation(user_query, case_file, model):
    prompt = (
        f"Your role is to act as a personal assistant on legal advices to users and to help clarify the prompts provided by the user. "
        f"Answer only according to the information given and under no circumstance must you provide the case files "
        f"unless specifically prompted and when prompted, give only the specific detail that's asked. "
        f"If the user merely greets or converses, don't bring up the case files. Using these conditions as a hard rule, "
        f"retrieve the case file given as:{case_file} and answer the users query in the best way possible, avoiding "
        f"ambiguity with the users query given as {user_query}."
    )

    response = model.send_message(prompt)
    return response.text

user_input = st.chat_input("Your message:", key="user_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    query_answer = query_obj.search_faiss(user_input)
    response = response_generation(user_input, query_answer, st.session_state.chat_model)

    st.session_state.messages.append({"role": "Verdict", "content": response})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
