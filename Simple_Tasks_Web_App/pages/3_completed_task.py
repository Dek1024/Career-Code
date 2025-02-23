import streamlit as st
import pandas as pd

conn = st.connection("postgresql", type="sql",ttl=0.01)
df = conn.query(f"SELECT * FROM task_database WHERE completed")
df = pd.DataFrame(df)
st.write(df)