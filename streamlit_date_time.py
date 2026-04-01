import streamlit as st 

from datetime import date 

st.title("exam count down")
today=date.today()

exam_date=st.date_input("select your exam date ")

days_left=exam_date-today

st.write("todays date :", today)
st.write("selected exam date:",exam_date)

if days_left.days > 0:
	st.success(f"you have {days_left.days} for exam")
elif days_left.days == 0:
	st.warning("your exam is today")
else : 
	st.error(f"exam was{-days_left.days} ago")
