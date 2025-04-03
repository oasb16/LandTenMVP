# streamlit_app.py

import streamlit as st
st.set_page_config(page_title="LandTen", layout="wide")

# ========================
# 🧠 LandTen MVP — SS1_Gate Auth Layer Integration
# ========================
from superstructures.ss1_gate.streamlit_frontend.ss1_gate_app import run_login
from superstructures.ss2_pulse.ss2_pulse_app import run_router
from superstructures.tracker import show_tracker

# ========================
# 🔐 Config
# ========================
CLIENT_ID = st.secrets.get("COGNITO_CLIENT_ID")
COGNITO_DOMAIN = "https://us-east-1liycxnadt.auth.us-east-1.amazoncognito.com"
REDIRECT_URI = "https://landtenmvpmainapp.streamlit.app/"

# ========================
# 🔐 Authentication Layer
# ========================
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    run_login()

# ========================
# 🔀 Persona Routing Post Login
# ========================
run_router()

# ========================
# 🔓 Logout Button
# ========================
if st.session_state.get("logged_in"):
    if st.sidebar.button("Logout"):
        logout_url = f"{COGNITO_DOMAIN}/logout?client_id={CLIENT_ID}&logout_uri={REDIRECT_URI}"
        
        # Clear session state keys
        for key in list(st.session_state.keys()):
            del st.session_state[key]

        # Show logout success + trigger redirect
        st.success("✅ You have been logged out.")
        st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{logout_url}\'" />', unsafe_allow_html=True)
        st.stop()  # Prevent further rendering after logout redirect

# ========================
# 📌 Sidebar Navigation
# ========================
st.sidebar.title("Navigation")

if st.session_state.get("logged_in"):
    app_mode = st.sidebar.radio("Choose an option:", [
        "Home",  
        "Tenant Chat", 
        "Landlord", 
        "Contractor", 
        "Protocol Tracker",
        "About"
    ])

    # ========================
    # 🎯 Role-Based Views
    # ========================
    if app_mode == "Home":
        st.title("Welcome to LandTen MVP.")
        user_email = st.session_state.get("email", "tenant@example.com")
        st.write(f"Welcome, **{user_email}**. You can now describe your issue.")
        st.write("Select an option from the sidebar to proceed.")
        st.write("Navigation Bar Persona separation coming soon.")

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
        st.subheader("📚 Documentation")
        st.markdown("[Docs](https://github.com/oasb16/LandTenMVP/tree/master/docs)")
        st.markdown("[Playbook](https://github.com/oasb16/LandTenMVP/blob/master/docs/LandTen_Playbook.md)")
        st.markdown("[Workflow](https://github.com/oasb16/LandTenMVP/blob/master/docs/workflow.md)")
        st.markdown("[Enhancements](https://github.com/oasb16/LandTenMVP/blob/master/docs/LandTen_Enhancements.md)")

else:
    st.sidebar.warning("🔐 Please log in with Google SSO to access LandTen features.")
