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

code = ''' Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)'''
st.code(code, language='python')

  

st.write("2. Splitting a string")

"""
If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!
"""


code = ''' string = “hello world”
string.split()'''
st.code(code, language='python')

st.write("3. Reversing a string")

"""
If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.
"""


code = ''' str=”hello world!”
a=str[::-1]
print(a)'''
st.code(code, language='python')