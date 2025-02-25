import streamlit as st
import psycopg2

id = st.text_input("task_id (number):")
title = st.text_input("task_title:")
description = st.text_input("task_description:")
start_date = st.text_input("Enter date in YYYY-MM-DD:")
end_date = st.text_input("enter date in YYYY-MM-DD:")

if st.button("create_task"):
    conn = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "skapeed24!)97")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO task_database(id,title,description,start_date,end_date) VALUES(%s,%s,%s,%s,%s);",(id,title,description,start_date,end_date))
    conn.commit()
    st.write("The task has been created successfully")
    conn.close()

if st.button("look at up updated rows"):
    conn = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "skapeed24!)97")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM task_database")
    answer = cursor.fetchall()
    st.dataframe(answer)
    conn.close()