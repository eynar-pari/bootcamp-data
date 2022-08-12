from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

st.title('Class 2 > Mojix bootcamp')

st.write("Tutorial")

st.write("Splitting a string")

"""
If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!
"""


with st.echo(code_location='below'):
   string = "hello world"
   string.split()