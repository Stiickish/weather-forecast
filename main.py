import streamlit as st

# Set the title for the program
st.title("Weather Forecast Prediction")

# Location input
location = st.text_input("Place: ")

# Forecast days slider
days = st.slider("Forecast in days", min_value=1, max_value=5,help="Select the number of desired days of weather forecasting")

options = st.selectbox("Select data to view",
                                  ("Temperature", "Sky"))

if days <= 1:
    st.subheader(f"{options} for the next {days} day in {location}")
else:
    st.subheader(f"{options} for the next {days} days in {location}")

