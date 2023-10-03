import streamlit as st
import pandas

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("images/pic.png", width=300)

with col2:

    st.title("DEV NARAYAN")
    content = """
    Hi, I am Dev Narayan! professional Python developer.
     I graduated in 2022 in the field of Electrical engineering from Haldia institute of technology.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact us!
"""
st.subheader(content2)



col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("venv/data.csv", sep=";")
with col3:
    for index,row in df[:10].iterrows():
        content=row["title"]
        st.header(content)
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index,row in df[10:].iterrows():
        content=row["title"]
        st.header(content)
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

