
import streamlit as st
import requests
import base64
import json
from urllib.parse import urlencode
from superstructures.ss1_gate.persona_extractor import extract_persona
from superstructures.ss1_gate.shared.dynamodb import write_user_profile

CLIENT_ID = "ud60jun60me7po0pj0u8uvu2v"
COGNITO_DOMAIN = "https://us-east-1liycxnadt.auth.us-east-1.amazoncognito.com"
REDIRECT_URI = "https://landtenmvpmainapp.streamlit.app/"
TOKEN_ENDPOINT = f"{COGNITO_DOMAIN}/oauth2/token"

def run_login():
    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        return

    query_params = st.query_params
    if "code" in query_params:
        code = query_params["code"][0]
        data = {
            "grant_type": "authorization_code",
            "client_id": CLIENT_ID,
            "code": code,
            "redirect_uri": REDIRECT_URI,
        }
        auth_header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(TOKEN_ENDPOINT, data=urlencode(data), headers=auth_header)
        if response.status_code == 200:
            token_data = response.json()
            id_token = token_data.get("id_token", "")
            payload_part = id_token.split(".")[1] + "==="
            padded = payload_part + '=' * (-len(payload_part) % 4)
            decoded = json.loads(base64.urlsafe_b64decode(padded.encode()).decode())
            email = decoded.get("email", "")
            persona = extract_persona()
            st.session_state["logged_in"] = True
            st.session_state["email"] = email
            st.session_state["persona"] = persona
            write_user_profile(email, persona)
            st.experimental_set_query_params()
        else:
            st.error("Login failed")
    else:
        login_url = (
            f"{COGNITO_DOMAIN}/login?response_type=code&client_id={CLIENT_ID}"
            f"&redirect_uri={REDIRECT_URI}&identity_provider=Google"
        )
        st.markdown(f"[Login with Google SSO]({login_url})")
