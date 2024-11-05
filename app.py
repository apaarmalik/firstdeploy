import streamlit as st
import pandas as pd
import numpy as np

num1 = st.numper_input("enter 1st number")
num2 = st.number_input("enter 2nd number")

num3 = num1 + num2


st.write("hello")
st.write(num3)
