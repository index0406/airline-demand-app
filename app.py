# app.py
import streamlit as st
import plotly.express as px
from data_fetcher import fetch_flight_data
from data_processor import process_flight_data

st.set_page_config(page_title="Airline Demand Tracker", layout="wide")
st.title("✈️ Airline Booking Market Demand Web App")

# -- Dropdown Filter --
airport_options = {
    "Sydney (SYD)": "SYD",
    "Melbourne (MEL)": "MEL",
    "Delhi (DEL)": "DEL",
    "Mumbai (BOM)": "BOM",
    "Brisbane (BNE)": "BNE",
    "Los Angeles (LAX)": "LAX",
    "New York (JFK)": "JFK",
    "London (LHR)": "LHR"
}

source_city = st.sidebar.selectbox("Select Source Airport", list(airport_options.keys()))
destination_city = st.sidebar.selectbox("Select Destination Airport", list(airport_options.keys()))
source = airport_options[source_city]
destination = airport_options[destination_city]

# API key input
api_key = st.sidebar.text_input("Enter your Aviationstack API Key", type="password")

if st.sidebar.button("Get Flight Data"):
    with st.spinner("Fetching flight data..."):
        data = fetch_flight_data(api_key, source, destination)
        df, hourly_trend = process_flight_data(data)

        if df is not None:
            st.subheader("📋 Raw Flight Data")
            st.dataframe(df[['airline.name', 'flight.iata', 'departure_time', 'arrival.scheduled']])

            st.subheader("📈 Departure Time Trend (by Hour)")
            fig = px.line(x=hourly_trend.index, y=hourly_trend.values, labels={"x": "Hour", "y": "Flights"})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No data found or invalid API key.")