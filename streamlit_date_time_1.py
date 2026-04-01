import streamlit as st
from datetime import date

st.title("Age Checker")

user_date = st.date_input("Enter your date of birth", format="YYYY-MM-DD")
today = date.today()

if st.button("Submit"):
    age = today.year - user_date.year

    if (today.month, today.day) < (user_date.month, user_date.day):
        age -= 1

    if age < 18:
        st.warning("He is under 18")
    elif age == 18:
        st.info("He is exactly 18")
    else:
        st.success("He is above 18")
			
