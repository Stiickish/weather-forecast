import streamlit as st
import plotly.express as px

# Set the title for the program
st.title("Weather Forecast Prediction")

# Location input
location = st.text_input("Place: ")

# Forecast days slider
days = st.slider("Forecast in days", min_value=1, max_value=5,
                 help="Select the number of desired days of weather forecasting")

# A dropdrown so user can change either temperature or sky
options = st.selectbox("Select data to view",
                       ("Temperature", "Sky"))

if days <= 1:
    st.subheader(f"{options} for the next {days} day in {location}")
else:
    st.subheader(f"{options} for the next {days} days in {location}")

date = ["2222-24-10", "2022-26-10", "2022-27-10", "2022-28-10", "2022-29-10"]
temperatures = [10, 8.5, 5, 7.6, 6.7]
temperatures = [days * i for i in temperatures]
figure = px.line(x=date, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
