import streamlit as st
import json
import os

def run_login():
    state_file = "shared/user_state.json"
    if os.path.exists(state_file):
        with open(state_file, "r") as f:
            user_data = json.load(f)
            st.session_state["logged_in"] = user_data.get("logged_in", False)
            st.session_state["email"] = user_data.get("email", "")
            st.session_state["persona"] = user_data.get("persona", "")
            st.success(f"Logged in as {st.session_state['email']} ({st.session_state['persona']})")
    else:
        st.warning("Not logged in. Please sign in or sign up.")
        st.markdown("[Sign In](http://localhost:5000/signin)")
        st.markdown("[Sign Up as Tenant](http://localhost:5000/signup?persona=tenant)")
        st.markdown("[Sign Up as Landlord](http://localhost:5000/signup?persona=landlord)")
        st.markdown("[Sign Up as Contractor](http://localhost:5000/signup?persona=contractor)")
