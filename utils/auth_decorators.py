import streamlit as st

def require_persona(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            persona = st.session_state.get("persona")
            if persona != required_role:
                st.error("Unauthorized: This page is restricted to " + required_role)
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator