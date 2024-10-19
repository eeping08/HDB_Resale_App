import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

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

# Sidebar for navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "About Us", "Methodology"])

if page == "Methodology":
    st.title("Methodology")
    st.write("### Data Flows and Implementation Details")
    st.write("In this section, we will explain the data flows and implementation details.")

st.write("""
The application consists of two main use cases:
- **User Input and Data Filtering**: Users input their budget, which is then used to filter the dataset of HDB resale flats. The application processes the input and returns a list of flats that fall within the specified budget.
- **Data Visualization**: After filtering, the application provides a visualization of the price distribution of the affordable flats, helping users understand the market better.
""")

st.write("### Implementation Details")
st.write("""
1. **Data Loading**: The application loads a CSV file containing the relevant data, including flat prices and ages.
2. **User Interface**: Streamlit is used to create a user-friendly interface with input fields and buttons.
3. **Data Processing**: Using Pandas, the application processes the data to filter and prepare it for visualization.
4. **Visualization**: Matplotlib and Seaborn libraries are used to create visual representations of the data.
""")

st.image("https://raw.githubusercontent.com/eeping08/HDB_Resale_App/refs/heads/main/Untitled%20Diagram.jpg")

if page == "Methodology":
    st.title("Methodology")
    st.write("### Data Flows and Implementation Details")
    st.write("""
    The application consists of two main use cases:
    - **User Input and Data Filtering**: Users input their budget, which is then used to filter the dataset of HDB resale flats. The application processes the input and returns a list of flats that fall within the specified budget.
    - **Data Visualization**: After filtering, the application provides a visualization of the price distribution of the affordable flats, helping users understand the market better.
    """)

    st.write("### Implementation Details")
    st.write("""
    1. **Data Loading**: The application loads a CSV file containing the relevant data, including flat prices and ages.
    2. **User Interface**: Streamlit is used to create a user-friendly interface with input fields and buttons.
    3. **Data Processing**: Using Pandas, the application processes the data to filter and prepare it for visualization.
    4. **Visualization**: Matplotlib and Seaborn libraries are used to create visual representations of the data.
    """)

    # Display flowchart image
    st.image("flowchart.png", caption="Flowchart for Data Flows and Use Cases")


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
    st.write("**About Us**\n\nThis project helps users find affordable HDB resale flats based on their budget in Singapore.The prices of the houses sold in Year 2015 and Year 2016 are obtained from www.data.gov.sg.")

if methodology:
    st.write("**Methodology**\n\nWe use data on resale flat prices and age of flat to provide insights on the cost of HDB flats around the central part of Singapore.")
