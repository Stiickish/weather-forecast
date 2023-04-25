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

# A dropdown so user can change either temperature or sky
options = st.selectbox("Select data to view",
                       ("Temperature", "Sky"))

# Condition check. Shows either day or days
if days <= 1:
    st.subheader(f"{options} for the next {days} day in {location}")
else:
    st.subheader(f"{options} for the next {days} days in {location}")

# Checks if there is a location.
if location:
    try:
        # Get the data from backend, location and days
        filtered_data = get_data(location, days)

        # Checks if user input is temperature
        # Temperature data is extracted and filtered
        # Data is plotted
        if options == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        # Checks if the user input is sky
        # Sky data is extracted and filtered
        # Using list comprehensions to map through the list of weather data
        # Using second list comprehensions to create image path corresponding to condition
        if options == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=100)
    except:
        st.info("No location found. Please enter a valid city")
