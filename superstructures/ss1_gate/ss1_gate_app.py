import streamlit as st
import requests
import json
import os
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = st.secrets.get("COGNITO_CLIENT_ID")
COGNITO_DOMAIN = st.secrets.get("COGNITO_DOMAIN")
REDIRECT_URI = st.secrets.get("REDIRECT_URI")
TOKEN_URL = f"https://{COGNITO_DOMAIN}/oauth2/token"

print(f" COGNITO_DOMAIN : {COGNITO_DOMAIN}")

def run_login():
    query_params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "identity_provider": "Google",
    }

    persona = st.query_params.get("persona", "tenant")
    st.session_state["persona"] = persona

    if "code" not in st.query_params:
        login_url = f"https://{COGNITO_DOMAIN}/login?{urlencode(query_params)}"
        st.markdown(f"[Login with Google SSO]({login_url})")
        st.stop()
    else:
        code = st.query_params["code"]
        token_response = requests.post(
            TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "client_id": CLIENT_ID,
                "redirect_uri": REDIRECT_URI
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        if token_response.ok:
            tokens = token_response.json()
            id_token = tokens.get("id_token", "")
            user_info = json.loads(
                requests.get(
                    f"https://{COGNITO_DOMAIN}/oauth2/userInfo",
                    headers={"Authorization": f"Bearer {tokens['access_token']}"}
                ).text
            )
            st.session_state["email"] = user_info.get("email")
            st.session_state["logged_in"] = True
            st.success(f"Logged in as {st.session_state['email']} ({persona})")
        else:
            st.error("Login failed")
            st.stop()
