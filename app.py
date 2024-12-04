import streamlit as st
import pandas as pd

# Sample Data (You can replace this with a database or actual data)
data = {
    "Client ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [25, 34, 45, 29, 40],
    "Last Visit": ["2023-10-15", "2023-10-20", "2023-11-05", "2023-11-12", "2023-11-25"],
    "Condition": ["Healthy", "Diabetes", "Hypertension", "Healthy", "Asthma"],
}
df = pd.DataFrame(data)

# Streamlit App
st.title("Clinic Client Dashboard")
st.sidebar.title("Options")

# Sidebar Options
view_data = st.sidebar.checkbox("View Client Data")
search_client = st.sidebar.checkbox("Search Client")

# View All Data
if view_data:
    st.subheader("All Client Data")
    st.dataframe(df)

# Search Client
if search_client:
    st.subheader("Search for a Client")
    client_id = st.number_input("Enter Client ID", min_value=1, max_value=len(df), step=1)
    client_data = df[df["Client ID"] == client_id]
    
    if not client_data.empty:
        st.write("Client Details:")
        st.write(client_data)
    else:
        st.warning("No client found with the given ID.")
        
st.sidebar.markdown("---")
st.sidebar.markdown("Developed for simple clinic data management.")
