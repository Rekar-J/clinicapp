import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Client ID": [1, 2, 3],
    "Name": ["Alice Smith", "Bob Johnson", "Charlie Brown"],
    "Age": [34, 45, 29],
    "Appointment Date": ["2024-12-05", "2024-12-06", "2024-12-07"],
    "Condition": ["Flu", "Back Pain", "Cold"],
}

df = pd.DataFrame(data)

# Sidebar menu
menu = ["Dashboard", "Client List", "Appointments", "About"]
st.sidebar.title("Clinic Menu")
selection = st.sidebar.radio("Navigate", menu)

if selection == "Dashboard":
    st.title("Clinic Data Dashboard")
    st.write("Welcome to the clinic dashboard. Below are some basic statistics.")
    
    st.write("### Client Statistics")
    st.write(f"Total Clients: {len(df)}")
    st.write(f"Average Age: {df['Age'].mean():.2f}")

    # Visualization
    fig, ax = plt.subplots()
    df['Age'].plot(kind='bar', ax=ax, title='Clients Age Distribution')
    ax.set_xlabel("Client ID")
    ax.set_ylabel("Age")
    st.pyplot(fig)

elif selection == "Client List":
    st.title("Client List")
    st.dataframe(df)

elif selection == "Appointments":
    st.title("Appointments")
    st.write("Below are the upcoming appointments:")
    st.dataframe(df[["Name", "Appointment Date", "Condition"]])

elif selection == "About":
    st.title("About the Clinic")
    st.write("""
        This is a simple clinic management system to view data and navigate between different functionalities.
        Developed using Streamlit for ease of use and interactivity.
    """)

# Footer
st.sidebar.write("---")
st.sidebar.write("Clinic Management App © 2024")
