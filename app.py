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


st.write("newline")

df_aux = df.describe(include='all')
st.write(df_aux)



tx = st.chat_input("Enter the text")
ctx = tx.split()
st.write(len(ctx))
i=0
for i in range(len(ctx)):
    if ctx[i]=="max":
        max = df["value"].max()
        st.write(f"The maximum value in the dataframe is {max}")
    else:
        st.write(f"Aska valid question")

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
