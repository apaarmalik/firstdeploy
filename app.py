import streamlit as st
num1=st.number_input("enter 1st number")
num2=st.number_input("enter 2nd number")
opr = st.chat_input("Enter the operator")

if opr == "+":
  st.write(num1+num2)
