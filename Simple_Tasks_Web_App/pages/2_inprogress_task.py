import streamlit as st
import psycopg2

conn = psycopg2.connect(host = "localhost",database = "postgres",user = "postgres",password = "skapeed24!)97")
cursor = conn.cursor()
cursor.execute("SELECT * FROM task_database WHERE NOT completed;")
database = cursor.fetchall()
st.dataframe(database)
#st.write("Successful commit to database")

id = st.text_input("Complete task (enter_task_id)")
user_confirmation = st.button("Confirm task completion ?")

if user_confirmation:
    cursor.execute("UPDATE task_database SET completed = (%s) WHERE id = (%s);",(True,id))
    conn.commit()
    st.audio("/Users/user/Career Code/Simple_Tasks_Web_App/files/task_complete.mp3",autoplay=True)
    st.write("Task completed")

st.page_link("pages/3_completed_task.py",label="Completed_Task(s)",icon = ":material/arrow_right_alt:")