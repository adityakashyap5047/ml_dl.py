import streamlit as st
import numpy as np
import pandas as pd

## Title of the application
st.title("Hello Streamlit")

# Display a simple Text
st.write("This is a simple Text")

# Create a simple DataFrame

df = pd.DataFrame({
    'First Column': [1, 2, 3, 4],
    'Second Column': [10, 20, 30, 40]
})

st.write("Here is the dataframe")
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)