from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import plotly.figure_factory as ffz

st.title('Class 2 > Mojix bootcamp')

st.subheader('Tutorial')


st.caption("1. Walrus operator")

"""
The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.
"""

st.write("Example")

code = ''' Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)'''
st.code(code, language='python')
st.write("Output")

code = '''3'''
st.code(code, language='python')

st.caption("2. Splitting a string")

"""
If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!
"""

st.write("Example")
code = ''' string = “hello world”
string.split()'''
st.code(code, language='python')
st.write("Output")

code = '''[‘hello’, ‘world’]'''
st.code(code, language='python')

st.caption("3. Reversing a string")

"""
If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.
"""

st.write("Example")
code = ''' str=”hello world!”
a=str[::-1]
print(a)'''
st.code(code, language='python')

st.write("Output")

code = '''!dlrow olleh'''
st.code(code, language='python')

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)


# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)