import streamlit as st
import urllib.parse
import os

def run_login():
    if "logged_in" not in st.session_state:
        st.title("🔐 LandTen — Sign In")

        # Extract persona from URL
        query_params = st.experimental_get_query_params()
        persona = query_params.get("persona", ["tenant"])[0]

        client_id = os.getenv("COGNITO_CLIENT_ID")
        domain = os.getenv("COGNITO_DOMAIN")
        redirect_uri = os.getenv("REDIRECT_URI")

        login_url = (
            f"https://{domain}/login?"
            + urllib.parse.urlencode({
                "response_type": "code",
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "identity_provider": "Google"
            })
        )

        st.session_state["persona"] = persona
        st.markdown(f"[🔐 Click here to login with Google SSO]({login_url})")
        st.stop()
