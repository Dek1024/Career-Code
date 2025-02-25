import streamlit as st
import psycopg2 

conn = psycopg2.connect(host = "localhost",database = "postgres", user = "postgres", password = "skapeed24!)97")
cursor = conn.cursor()
cursor.execute("SELECT * FROM task_database WHERE completed")
returned_info = cursor.fetchall()
st.dataframe(returned_info)