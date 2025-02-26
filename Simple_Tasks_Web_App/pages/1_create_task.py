import streamlit as st
import psycopg2

id = st.text_input("task_id (number):")
title = st.text_input("task_title:")
description = st.text_input("task_description:")
start_date = st.text_input("Enter date in YYYY-MM-DD:")
end_date = st.text_input("enter date in YYYY-MM-DD:")

if st.button("create_task"):
    conn = psycopg2.connect(host = st.secrets.connections.host, 
                            database = st.secrets.connections.database,
                              user = st.secrets.connections.username, 
                              password = st.secrets.connections.password)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO task_database(id,title,description,start_date,end_date) VALUES(%s,%s,%s,%s,%s);",(id,title,description,start_date,end_date))
    conn.commit()
    st.write("The task has been created successfully")
    conn.close()

st.page_link("pages/2_inprogress_task.py",label="Inprogress_Task(s)",icon = ":material/arrow_right_alt:")
st.page_link("home_window.py",label="Home_Window",icon = ":material/arrow_right_alt:")
