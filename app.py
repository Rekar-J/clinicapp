import streamlit as st
import pandas as pd

# App title and description
st.title("Clinic Data Dashboard")
st.markdown("""
Welcome to the Clinic Data Dashboard. 
Upload your client data file to get started. The dashboard provides:
- Quick data overview
- Key metrics
- Search and filter functionality
""")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Load the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the uploaded data
    st.subheader("Uploaded Data")
    st.write(df.head())

    # Show basic stats
    st.subheader("Key Metrics")
    st.write("Total Records:", len(df))
    if 'Age' in df.columns:
        st.write("Average Age:", df['Age'].mean())
    if 'Gender' in df.columns:
        st.write("Gender Distribution:")
        st.bar_chart(df['Gender'].value_counts())

    # Search functionality
    st.subheader("Search Clients")
    if 'Name' in df.columns:
        search_term = st.text_input("Enter a client name to search:")
        if search_term:
            search_results = df[df['Name'].str.contains(search_term, case=False, na=False)]
            st.write(search_results)
        else:
            st.write("Enter a name to search in the data.")

    # Download filtered data
    st.subheader("Download Filtered Data")
    st.markdown("Use the search feature above to filter data.")
    if 'search_results' in locals():
        csv = search_results.to_csv(index=False)
        st.download_button(
            label="Download Filtered Data",
            data=csv,
            file_name="filtered_data.csv",
            mime="text/csv"
        )
else:
    st.write("Upload a CSV file to start analyzing data.")

# Footer
st.markdown("---")
st.markdown("Powered by Streamlit")
