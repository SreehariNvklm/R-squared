import streamlit as st
from src.database.db_query import DB_Query
from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv()

st.set_page_config(page_title="Verdict Chat",page_icon=":speech_balloon:")

def response_generation(user_query,case_file,model):
    history = []
    prompt = (
        f"Your role is to act as a personal assistant to users and to help clarify the prompts provided by the user. "
        f"Answer only according to the information given and under no circumstance must you provide the case files "
        f"unless specifically prompted and when prompted, give only the specific detail that's asked. "
        f"If the user merely greets or converses, don't bring up the case files. Using these conditions as a hard rule, "
        f"retrieve the case file given as:{case_file} and answer the users query in the best way possible, avoiding "
        f"ambiguity with the users query given as {user_query}")
    # prompt = (f"Given the retrieved case file according to the user query: {user_query}, case file: {case_file}. Analyze the retrieved file and converse with the user only according"
              # f" to the user query. Don't give case file details even if obtained when the user greets you and on these specific occasions.")

    response = model.send_message(prompt)
    history.append(response.text)
    return response.text

if "messages" not in st.session_state or "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.messages = []

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
chat_model = model.start_chat(history=st.session_state.chat_history)
query_obj = DB_Query()

user_input = st.chat_input("Your message:",key="user_input")

if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    query_answer = query_obj.search_faiss(user_input)
    response = response_generation(user_input, query_answer,chat_model)
    st.session_state.messages.append({"role":"Verdict","content":response})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])