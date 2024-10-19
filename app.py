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
    
# Data Visualization: Scatter Plot of Resale Price vs Remaining Lease
if not filtered_data.empty:
    st.write("Scatter Plot: Resale Price vs Remaining Lease")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=filtered_data, x='resale_price', y='remaining_lease', hue='flat_type')
    plt.xlabel("Resale Price ($)")
    plt.ylabel("Remaining Lease (Years)")
    plt.title("Resale Price vs Remaining Lease")
    st.pyplot(plt)
else:
    st.write("No houses found within your budget.")

# Sidebar for user input
budget = st.sidebar.number_input("Enter your budget (SGD):", min_value=0)
flat_age = st.sidebar.slider("Select the maximum age of the flat:", 0, 99)

# Sidebar for navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "About Us", "Methodology"])

# Load hawker centres data
hawker_data = gpd.read_file("hawker_centres.geojson")

# Function to find hawker centres near selected HDB street
def find_hawker_centres(street_name, hawker_data):
    # Filter hawker centres based on street name or nearby areas
    nearby_hawkers = hawker_data[hawker_data['address'].str.contains(street_name, case=False, na=False)]
    return nearby_hawkers

# Display hawker centres based on user selection
if page == "HDB Resale Search":
    st.title("Find HDBs and Nearby Hawker Centres")
    budget = st.number_input("Enter your budget (SGD):", min_value=0, max_value=1000000, step=1000)
    street_name = st.text_input("Enter the HDB street name to search for nearby hawker centres:")

# Display HDBs within budget
filtered_hdbs = data[(data['resale_price'] <= budget)]
st.write(filtered_hdbs)

# Create a dropdown for users to select a street name from the filtered results
if not filtered_hdbs.empty:
    street_name = st.selectbox("Select a street name to find nearby hawker centres:", filtered_hdbs['street_name'].unique())
else:
    street_name = None

# Check if a street name has been selected
if street_name:
    hawker_centres_nearby = find_hawker_centres(street_name, hawker_data)
    st.write("Nearby Hawker Centres:")
    st.write(hawker_centres_nearby[['name', 'address']])

# Display hawker centres near the selected street name
if street_name:
    hawker_centres_nearby = find_hawker_centres(street_name, hawker_data)
    st.write("Nearby Hawker Centres:")
    st.write(hawker_centres_nearby[['name', 'address']])

def find_hawker_centres(street_name, hawker_data):
    # filter hawker centres within a certain distance of the street
    return hawker_data[hawker_data['street_name'].str.contains(street_name, case=False)]


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
1. **Data Loading**: The application loads a CSV file containing the relevant data, including flat resale prices and ages.
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
