import streamlit as st

def extract_persona():
    return st.session_state.get("persona", "tenant")
