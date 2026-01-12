import streamlit as st

st.title("Power Calculator App")

# Take input from user
num = st.number_input("Enter a number:", value=0)

# Calculate results
square = num ** 2
cube = num ** 3
power_5 = num ** 5

# Display results
st.write(f"Square of {num} = {square}")
st.write(f"Cube of {num} = {cube}")
st.write(f"{num} to the power 5 = {power_5}")
