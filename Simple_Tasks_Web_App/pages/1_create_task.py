import streamlit as st
import psycopg2
#from google.cloud import secretmanager

id = st.text_input("task_id (number):")
title = st.text_input("task_title:")
description = st.text_input("task_description:")
start_date = st.text_input("Enter date in YYYY-MM-DD:")
end_date = st.text_input("enter date in YYYY-MM-DD:")

# Fetch database credentials from Cloud Secret Manager
# secret_client = secretmanager.SecretManagerServiceClient()
# secret_name = "projects/74864121827/secrets/cloudsql-credentials/versions/latest"
# response = secret_client.access_secret_version(request={"name": secret_name})
# credentials = response.payload.data.decode("UTF-8")
if st.button("create_task"):
    conn = psycopg2.connect(host = st.secrets.connections.host, 
                            database = st.secrets.connections.database,
                              user = st.secrets.connections.username, 
                              password = st.secrets.connections.password)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO tasktracker_table (id,title,description,start_date,end_date) VALUES(%s,%s,%s,%s,%s);",(id,title,description,start_date,end_date))
    conn.commit()
    st.write("The task has been created successfully")
    conn.close()

st.page_link("pages/2_inprogress_task.py",label="Inprogress_Task(s)",icon = ":material/arrow_right_alt:")
st.page_link("home_window.py",label="Home_Window",icon = ":material/arrow_right_alt:")