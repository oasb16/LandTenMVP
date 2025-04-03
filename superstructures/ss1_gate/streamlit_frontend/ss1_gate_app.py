
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
CLIENT_SECRET

import streamlit as st
import requests
import jwt
import base64

def run_login():
    query_params = st.query_params

    if "code" in query_params:
        code = query_params["code"]

        token_url = "https://us-east-1liycxnadt.auth.us-east-1.amazoncognito.com/oauth2/token"
        client_id = "ud60jun60me7po0pj0u8uvu2v"
        client_secret = "YOUR_CLIENT_SECRET"
        redirect_uri = "https://landtenmvpmainapp.streamlit.app/"

        # Base64 encode client_id:client_secret
        basic_auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {basic_auth}"
        }

        payload = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
        }

        res = requests.post(token_url, data=payload, headers=headers)

        if res.status_code == 200:
            tokens = res.json()
            id_token = tokens.get("id_token", "")
            user_info = jwt.decode(id_token, options={"verify_signature": False})

            st.session_state["logged_in"] = True
            st.session_state["email"] = user_info.get("email", "")
            st.session_state["persona"] = st.query_params.get("persona", "tenant")

            st.experimental_set_query_params()
            st.rerun()
        else:
            st.error(f"Login failed: {res.text}")
    else:
        login_url = f"https://us-east-1liycxnadt.auth.us-east-1.amazoncognito.com/login?client_id={client_id}&response_type=code&scope=email+openid+phone&redirect_uri={redirect_uri}"
        st.markdown(f"[Login with Google SSO]({login_url})")

