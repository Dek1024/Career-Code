import streamlit as st
import psycopg2

conn = psycopg2.connect(host = "localhost",database = "postgres",user = "postgres",password = "skapeed24!)97")
cursor = conn.cursor()
cursor.execute("SELECT * FROM task_database WHERE NOT completed;")
database = cursor.fetchall()
st.dataframe(database)
st.write("Successful commit to database")

id = st.text_input("Complete task (enter_task_id)")
if id:
    cursor.execute("INSERT INTO task_database (completed) VALUES (%s) WHERE id = (%s);",(True,bool(id)))
    udpate = cursor.fetchall()

st.page_link("pages/3_completed_task.py",label="Completed_Task(s)",icon = ":material/arrow_right_alt:")