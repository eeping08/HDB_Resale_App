import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("HDB Resale Flat Explorer")

# Load the data
data = pd.read_csv('hdb_data.csv')

# Display the data
st.write(data.head())

# Input for budget
budget = st.number_input("Enter your budget:", min_value=0)

# Filter data based on budget
filtered_data = data[data['resale_price'] <= budget]

# Display the filtered data
if not filtered_data.empty:
    st.write("You can afford the following houses:")
    st.dataframe(filtered_data)
    
    # Visualization of price distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_data['resale_price'], bins=10, kde=True)
    plt.title('Price Distribution of Affordable Houses')
    plt.xlabel('resale_price')
    plt.ylabel('Frequency')
    st.pyplot(plt)  # Use Streamlit to display the plot
else:
    st.write("No houses found within your budget.")

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
    st.write("**About Us**\n\nThis project helps users find affordable HDB resale flats based on their budget in Singapore.")

if methodology:
    st.write("**Methodology**\n\nWe use data on resale flat prices and age of flat to provide insights on the cost of HDB flats around the central part of Singapore.")
