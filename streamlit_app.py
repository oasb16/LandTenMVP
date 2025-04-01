# streamlit_app.py
import streamlit as st
st.set_page_config(page_title="LandTen", layout="wide")
from superstructures.tracker import show_tracker

# Sidebar Navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Choose an option:", ["Home", "Protocol Tracker", "Tenant Chat", "Landlord", "Contractor","About"])

if app_mode == "Home":
    st.title("Welcome to LandTen MVP")
    st.write("This is Admin View.")
    st.write("Select an option from the sidebar to proceed.")
    st.write("Navigation Bar Person to have Login and Seperate view sooon.")


elif app_mode == "Protocol Tracker":
    show_tracker()

elif app_mode == "Tenant Chat":
    from superstructures.ss3_echo import run_echo
    run_echo()

elif app_mode == "Landlord":
    from superstructures.ss3_echo import run_echo
    run_echo()

elif app_mode == "Contractor":
    from superstructures.ss3_echo import run_echo
    run_echo()

elif app_mode == "About":
    st.write("Refer Docs: https://github.com/oasb16/LandTenMVP/tree/master/docs")
    st.write("Playbook : https://github.com/oasb16/LandTenMVP/blob/master/docs/LandTen_Playbook.md")
    st.write("Workflow : https://github.com/oasb16/LandTenMVP/blob/master/docs/workflow.md")