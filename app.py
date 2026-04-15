import streamlit as st

with open("kura_daily_works_form.html", "r") as f:
    html = f.read()

st.set_page_config(page_title="KURA Daily Works Form", layout="wide")
st.components.v1.html(html, height=2000, scrolling=True)
