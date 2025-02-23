import streamlit as st

conn = st.connection("postgresql", type="sql",ttl=0.01)

id = st.text_input("task_id (number):")
title = st.text_input("task_title:")
description = st.text_input("task_description:")
start_date = st.text_input("Enter date in YYYY-MM-DD:")
end_date = st.text_input("enter date in YYYY-MM-DD:")

if st.button("create_task"):
    params = {"id":id,"title":title,"description":description,"start_date":start_date,"end_date":end_date}
    df = conn.query(f"INSERT INTO task_database(id,title,description,start_date,end_date)VALUES(:id,:title,:description,:start_date,:end_date)",params = params)
    conn.commit()

