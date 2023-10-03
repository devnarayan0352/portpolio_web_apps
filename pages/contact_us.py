import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    option = st.selectbox(
        'What topic do you want to discuss?',
        df["topic"])
    raw_message = st.text_area("Text")
    message = f"""\
Subject: {option}

Hi there!
{user_email}

Thank you so much for your concerns.

our team will contact you shortly.


Thanks & regards,
Portfolio project team

"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_email, message)
        st.info("Your email was sent successfully")



