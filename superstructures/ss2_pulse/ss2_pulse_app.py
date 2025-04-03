import streamlit as st
from superstructures.ss2_pulse.router import route_user

def run_router():
    if not st.session_state.get("logged_in"):
        st.warning("Please log in first.")
        return

    persona = st.session_state.get("persona")
    route_user(persona)
