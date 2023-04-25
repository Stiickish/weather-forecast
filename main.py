import streamlit as st
import plotly.express as px
from backend import get_data

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

if location:
    # Get the data from backend
    filtered_data = get_data(location, days)

    if options == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if options == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=100)
