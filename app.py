import streamlit as st
import pandas as pd

st.title("🚗 Car Sales Data Analysis")

# Upload Excel file
uploaded_file = st.file_uploader("Upload your Car Sales Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
    
    # Show raw data
    st.subheader("Raw Data")
    st.dataframe(df)

    # Show basic stats
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Show column info
    st.subheader("Columns Available")
    st.write(df.columns.tolist())

    # Optional chart
    numeric_cols = df.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 0:
        st.subheader("Quick Chart")
        chart_col = st.selectbox("Select a numeric column to plot", numeric_cols)
        st.line_chart(df[chart_col])
else:
    st.info("Please upload an Excel file to start.")
