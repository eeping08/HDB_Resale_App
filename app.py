import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

# Title of the app
st.title("HDB Resale Flat Explorer")

# Load the HDB resale data
@st.cache_data
def load_data():
    hdb_data = pd.read_csv('hdb_data.csv') 
    return hdb_data

# Load the data
hdb_data = load_data()
# Load the data
data = pd.read_csv('hdb_data.csv')
hawker_data = gpd.read_file("hawker_centres.geojson")

# Display the data
st.write(data.head())

# Input for user budget
budget = st.number_input("Enter your budget:", min_value=0)

# Filter data based on budget
filtered_hdb = data[data['resale_price'] <= budget]

# Display the filtered data
if not filtered_hdb.empty:
    st.write("You can afford the following houses:")
    st.dataframe(filtered_hdb)

# Data Visualization: Scatter Plot of Resale Price vs Remaining Lease
if not filtered_hdb.empty:
    st.write("Scatter Plot: Resale Price vs Remaining Lease")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=filtered_hdb, x='resale_price', y='remaining_lease', hue='flat_type')
    plt.xlabel("Resale Price ($)")
    plt.ylabel("Remaining Lease (Years)")
    plt.title("Resale Price vs Remaining Lease")
    st.pyplot(plt)
else:
    st.write("No houses found within your budget.")

# Allow user to select a street name
if not filtered_hdb.empty:
    street_name = st.selectbox("Select a street name to find flat_model:", filtered_hdb['street_name'].unique())
else:
    street_name = None


hdb_df = pd.DataFrame(data)

# Add a select box for users to choose a street
selected_street = st.selectbox("Select a Street Name:", hdb_df['street_name'].unique())

# Filter the DataFrame based on the selected street
filtered_hdb= hdb_df[hdb_df['street_name'] == selected_street]

# Show a table with the filtered `flat_model`
if not filtered_flats.empty:
    st.write("Flat Models for the selected street:")
    st.write(filtered_hdb[['flat_model']])
else:
    st.write("No flats found for the selected street.")

# Sidebar for user input
budget = st.sidebar.number_input("Enter your budget (SGD):", min_value=0)
flat_age = st.sidebar.slider("Select the maximum age of the flat:", 0, 99)

# Sidebar for navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "About Us", "Methodology"])

# Display affordable HDBs based on user selection
if page == "HDB Resale Search":
    st.title("Find HDBs and Nearby Hawker Centres")
    budget = st.number_input("Enter your budget (SGD):", min_value=0, max_value=1000000, step=1000)
    street_name = st.text_input("Enter the HDB street name to search for flat model in the selected street:")

# Display HDBs within budget
filtered_hdb = data[(data['resale_price'] <= budget)]
st.write(filtered_hdb)

if page == "Methodology":
    st.title("Methodology")
    st.write("### Data Flows and Implementation Details")
    st.write("In this section, we will explain the data flows and implementation details.")


if page == "Methodology":
    st.title("Methodology")
    st.write("### Data Flows and Implementation Details")
    st.write("""
    The application consists of two main use cases:
    - **User Input and Data Filtering**: Users input their budget, which is then used to filter the dataset of HDB resale flats. The application processes the input and returns a list of flats that fall within the specified budget.
    - **Data Visualization**: After filtering, the application provides a visualization of the price distribution of the affordable flats, helping users understand the market better.
    """)

# Display data and plot
st.subheader("Filtered Flats")
st.write(filtered_hdb)

# About Us and Methodology pages
about_us = st.sidebar.button("About Us")
methodology = st.sidebar.button("Methodology")

if about_us:
    st.write("**About Us**\n\nThis project helps users find affordable HDB resale flats based on their budget in Singapore.The prices of the houses sold in Year 2015 and Year 2016 are obtained from www.data.gov.sg. The data includes the type of house and the level of the flat.")

if methodology:
    st.write("**Methodology**\n\nWe use data on resale flat prices and age of flat to provide insights on the cost of HDB resale flats around the central part of Singapore. The year format in the CSV data is formated for the purpose of better data handling.")

    st.write("### Implementation Details")
    st.write("""
    1. **Data Loading**: The application loads a CSV file containing the relevant data, including flat prices and ages.
    2. **User Interface**: Streamlit is used to create a user-friendly interface with input fields and buttons.
    3. **Data Processing**: Using Pandas, the application processes the data to filter and prepare it for visualization.
    4. **Visualization**: Matplotlib and Seaborn libraries are used to create visual representations of the data.
    """)

    # Display flowchart image
    st.image("flowchart.png", caption="Flowchart for Data Flows and Use Cases")

st.image("https://raw.githubusercontent.com/eeping08/HDB_Resale_App/refs/heads/main/Untitled%20Diagram.drawio.png")
