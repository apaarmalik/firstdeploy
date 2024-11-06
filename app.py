import streamlit as st
import pandas as pd
import openpyxl as px
import os
import io


while True:
    try:
        file = st.file_uploader("Select an excel File", accept_multiple_files=False)
        break
    except ValueError:
        print(" ")

try:
    df = pd.read_excel(file)
except:
    df = pd.read_csv(file)
st.write(df.head())

buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

num1=st.number_input("enter 1st number")
num2=st.number_input("enter 2nd number")
opr = st.chat_input("Enter the operator")

if opr!="":
    if opr == "+":
        st.write(num1+num2)
    elif opr == "*" or opr =="x":
        st.write(num1*num2)
    elif opr == "/":
        st.write(num1/num2)
    elif opr == "-":
        st.write(num1 - num2)
else:
  st.write(" ")
