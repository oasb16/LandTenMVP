import streamlit as st
st.set_page_config(layout="wide")  # ✅ MUST come first

from protocol_tracker.landten_protocol_tracker_app import render_tracker

st.sidebar.title("🧭 LandTen Shell")
persona = st.sidebar.radio("Choose Persona", ["tenant", "landlord", "contractor", "admin"])

if persona == "tenant":
    st.header("Tenant Interface (SS3)")
elif persona == "landlord":
    st.header("Landlord Dashboard (SS5 + SS6)")
elif persona == "contractor":
    st.header("Contractor Interface (SS7)")
elif persona == "admin":
    render_tracker()
 