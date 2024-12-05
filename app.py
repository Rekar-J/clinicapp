import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
patients_data = {
    "Client ID": [1, 2, 3, 4],
    "Name": ["Alice Smith", "Bob Johnson", "Charlie Brown", "Diana Adams"],
    "Age": [34, 45, 29, 55],
    "Appointment Date": ["2024-12-05", "2024-12-06", "2024-12-07", "2024-12-08"],
    "Condition": ["Flu", "Back Pain", "Cold", "Hypertension"],
}

medics_data = {
    "Medic ID": [101, 102, 103],
    "Name": ["Dr. Green", "Dr. White", "Dr. Black"],
    "Specialization": ["Flu", "Back Pain", "Hypertension"],
    "Available": ["Yes", "Yes", "No"],
}

patients_df = pd.DataFrame(patients_data)
medics_df = pd.DataFrame(medics_data)

# Sidebar menu
menu = ["Dashboard", "Client List", "Appointments", "Filter by Patient", "Available Medics", "About"]
st.sidebar.title("Clinic Menu")
selection = st.sidebar.radio("Navigate", menu)

if selection == "Dashboard":
    st.title("Clinic Data Dashboard")
    st.write("Welcome to the clinic dashboard. Below are some basic statistics.")
    
    st.write("### Client Statistics")
    st.write(f"Total Clients: {len(patients_df)}")
    st.write(f"Average Age: {patients_df['Age'].mean():.2f}")

    # Visualization
    fig, ax = plt.subplots()
    patients_df['Age'].plot(kind='bar', ax=ax, title='Clients Age Distribution')
    ax.set_xlabel("Client ID")
    ax.set_ylabel("Age")
    st.pyplot(fig)

elif selection == "Client List":
    st.title("Client List")
    st.dataframe(patients_df)

elif selection == "Appointments":
    st.title("Appointments")
    st.write("Below are the upcoming appointments:")
    st.dataframe(patients_df[["Name", "Appointment Date", "Condition"]])

elif selection == "Filter by Patient":
    st.title("Filter Clients by Name")
    search_name = st.text_input("Enter client name (or part of it):")
    if search_name:
        filtered_df = patients_df[patients_df["Name"].str.contains(search_name, case=False, na=False)]
        if not filtered_df.empty:
            st.write("### Matching Clients")
            st.dataframe(filtered_df)
        else:
            st.write("No matching clients found.")

elif selection == "Available Medics":
    st.title("Available Medics by Condition")
    condition = st.selectbox("Select a condition to view available medics:", patients_df["Condition"].unique())
    if condition:
        available_medics = medics_df[(medics_df["Specialization"] == condition) & (medics_df["Available"] == "Yes")]
        if not available_medics.empty:
            st.write(f"### Medics Available for {condition}")
            st.dataframe(available_medics[["Name", "Specialization"]])
        else:
            st.write(f"No medics currently available for {condition}.")

elif selection == "About":
    st.title("About the Clinic")
    st.write("""
        This is an advanced clinic management system designed to provide:
        - Data filtering capabilities
        - Insights into available medics
        - Client and appointment details
        - Interactive dashboards for enhanced usability
    """)
    st.write("Developed using Streamlit for a user-friendly experience.")

# Footer
st.sidebar.write("---")
st.sidebar.write("Clinic Management App © 2024")
