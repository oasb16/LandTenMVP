import streamlit as st

def run_router():
    if not st.session_state.get("logged_in"):
        st.warning("Please log in first.")
        return

    persona = st.session_state.get("persona")
    
    if persona == "tenant":
        from superstructures.ss3_echo import run_echo
        run_echo()
    elif persona == "landlord":
        from superstructures.ss5_view import run_view
        run_view()
    elif persona == "contractor":
        from superstructures.ss7_bind import run_bind
        run_bind()
    elif persona == "admin":
        from protocol_tracker.landten_protocol_tracker_app import render_tracker
        render_tracker()
    else:
        st.error("Unknown persona. Cannot route.")
