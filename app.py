import pandas as pd

# Load the data
data = pd.read_csv('hdb_data.csv')

# Check the first few rows of the data (optional)
st.write(data.head())

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("HDB Resale Flat Explorer")

# Sidebar for user input
budget = st.sidebar.number_input("Enter your budget (SGD):", min_value=0)
flat_age = st.sidebar.slider("Select the maximum age of the flat:", 0, 99)

# Sample logic: Replace with your data loading and filtering
data = pd.DataFrame({
    "Location": ["Area A", "Area B", "Area C"],
    "Price": [300000, 400000, 500000],
    "Age": [10, 20, 30]
})

filtered_data = data[(data["Price"] <= budget) & (data["Age"] <= flat_age)]

# Display data and plot
st.subheader("Filtered Flats")
st.write(filtered_data)

# About Us and Methodology pages
about_us = st.sidebar.button("About Us")
methodology = st.sidebar.button("Methodology")

if about_us:
    st.write("**About Us**\n\nThis project helps users find affordable HDB resale flats...")

if methodology:
    st.write("**Methodology**\n\nWe use data on resale flat prices and ages to provide insights...")
