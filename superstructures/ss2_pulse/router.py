import streamlit as st
from superstructures.ss3_echo import run_tenant_view
from superstructures.ss4_root.landlord_view import run_landlord_view
from superstructures.ss4_root.contractor_view import run_contractor_view
from protocol_tracker.landten_protocol_tracker_app import render_tracker

def route_user(persona: str):
    if persona == "tenant":
        run_tenant_view()
    elif persona == "landlord":
        run_landlord_view()
    elif persona == "contractor":
        run_contractor_view()
    elif persona == "admin":
        render_tracker()
    else:
        st.error("Invalid persona.")
