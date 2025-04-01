# streamlit_app.py
import streamlit as st
from superstructures.tracker import show_tracker

st.set_page_config(page_title="LandTen MVP", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Choose an option:", ["Home", "Protocol Tracker", "Tenant Chat"])

if app_mode == "Home":
    st.title("Welcome to LandTen MVP")
    st.write("Select an option from the sidebar to proceed.")

elif app_mode == "Protocol Tracker":
    show_tracker()

elif app_mode == "Tenant Chat":
    from superstructures.ss3_echo import run_echo
    run_echo()