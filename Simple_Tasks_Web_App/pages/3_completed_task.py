import streamlit as st
import psycopg2 
from pathlib import Path

conn = psycopg2.connect(host = st.secrets.connections.host, 
                            database = st.secrets.connections.database,
                              user = st.secrets.connections.username, 
                              password = st.secrets.connections.password)
cursor = conn.cursor()
cursor.execute("SELECT * FROM tasktracker_table WHERE completed")
returned_info = cursor.fetchall()
st.dataframe(returned_info)

id = st.text_input("Task id of task to be moved to in-progress chart")
new_end_date = st.text_input("Enter the new_end_date - format YYYY-MM-DD")
user_confirmation = st.button("Task Move to In-progress, Confirm ?")

if user_confirmation:
    cursor.execute("UPDATE tasktracker_table SET completed = %s, end_date = %s WHERE id = %s;",(False,new_end_date,id))
    conn.commit()
    path = Path(__file__).parent/"files/task_move_inprogress.mp3"
    st.write(path)
    st.audio(path,format = "audio/mpeg",autoplay=True)
    st.text("Task moved to inprogress")

st.page_link("pages/2_inprogress_task.py",label="Inprogress_Task(s)",icon = ":material/arrow_right_alt:")
st.page_link("home_window.py",label="Home_Window",icon = ":material/arrow_right_alt:")