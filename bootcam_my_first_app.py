from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

st.title('Class 2 > Mojix bootcamp')

st.subheader('Tutorial')


st.write("1. Walrus operator")

"""
The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.
"""



with st.echo(code_location='below'):
   Mylist = [1,2,3]
   if(l := len(mylist) > 2)
   print(l)



st.write("2. Splitting a string")

"""
If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!
"""


with st.echo(code_location='below'):
   string = "hello world"
   string.split()