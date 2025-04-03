# streamlit_app.py
import streamlit as st

# ========================
# 🧠 LandTen MVP — SS1_Gate Auth Layer Integration
# ========================

from superstructures.ss1_gate.streamlit_frontend.ss1_gate_app import run_login

# Trigger login if not already authenticated
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    run_login()
    st.stop()

# Post-login routing to persona-specific dashboard (SS2)
from superstructures.ss2_pulse.ss2_pulse_app import run_router
run_router()


st.set_page_config(page_title="LandTen", layout="wide")
from superstructures.tracker import show_tracker

# Sidebar Navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Choose an option:", ["Home",  "Tenant Chat", "Landlord", "Contractor", "Protocol Tracker","About"])

if app_mode == "Home":
    st.title("Welcome to LandTen MVP Admin View.")
    st.write("Select an option from the sidebar to proceed.")
    st.write("Navigation Bar Person to have Login and Seperate view sooon.")

elif app_mode == "Tenant Chat":
    from superstructures.ss3_echo import run_echo
    run_echo()

elif app_mode == "Landlord":
    from superstructures.ss3_echo import run_echo
    run_echo()

elif app_mode == "Contractor":
    from superstructures.ss3_echo import run_echo
    run_echo()

elif app_mode == "Protocol Tracker":
    show_tracker()

elif app_mode == "About":
    st.write("Refer Docs: https://github.com/oasb16/LandTenMVP/tree/master/docs")
    st.write("Playbook : https://github.com/oasb16/LandTenMVP/blob/master/docs/LandTen_Playbook.md")
    st.write("Workflow : https://github.com/oasb16/LandTenMVP/blob/master/docs/workflow.md")
    st.write("Future Enhancements : https://github.com/oasb16/LandTenMVP/blob/master/docs/LandTen_Enhancements.md")
    