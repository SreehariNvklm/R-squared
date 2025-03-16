from src.database.db_query import DB_Query
import streamlit as st

st.set_page_config(page_title="Project Verdict",page_icon=":grey_question:")
st.header("Project Verdict")
st.write("Search case files:")

user_input = st.text_input("Enter the case: ")
btn = st.button("Fetch Case Files")
if btn and user_input:
    query_obj = DB_Query()
    st.write(query_obj.search_faiss(user_input,1))