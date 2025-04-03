import streamlit as st
import requests
import base64
import json
from datetime import datetime
import jwt
from urllib.parse import urlencode
from superstructures.ss1_gate.persona_extractor import extract_persona
from superstructures.ss1_gate.shared.dynamodb import write_user_profile

CLIENT_ID = st.secrets.get("COGNITO_CLIENT_ID")
COGNITO_CLIENT_SECRET = st.secrets.get("COGNITO_CLIENT_SECRET")
COGNITO_DOMAIN = "https://us-east-1liycxnadt.auth.us-east-1.amazoncognito.com"
REDIRECT_URI = "https://landtenmvpmainapp.streamlit.app/"
TOKEN_ENDPOINT = f"{COGNITO_DOMAIN}/oauth2/token"

def run_login():
    if "persona" not in st.session_state:
        st.session_state["persona"] = st.selectbox("Choose your role", ["tenant", "landlord", "contractor"])
        
    query_params = st.query_params
    code = query_params.get("code", None)
    persona = query_params.get("persona", "tenant")  # default to tenant

    if code:
        # Construct Basic Auth
        basic_auth = base64.b64encode(f"{CLIENT_ID}:{COGNITO_CLIENT_SECRET}".encode()).decode()
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {basic_auth}"
        }

        payload = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
        }

        try:
            res = requests.post(TOKEN_ENDPOINT, data=payload, headers=headers)

            if res.status_code == 200:
                tokens = res.json()
                id_token = tokens.get("id_token", "")
                user_info = jwt.decode(id_token, options={"verify_signature": False})

                # Update session state
                st.session_state["logged_in"] = True
                st.session_state["email"] = user_info.get("email", "")
                st.session_state["persona"] = persona

                #Storing to DB
                user_profile = {
                    "email": st.session_state["email"],
                    "persona": persona,
                    "login_source": "GoogleSSO",
                    "timestamp": str(datetime.utcnow().isoformat())
                }
                write_user_profile(user_profile)

                # Remove query params from URL
                st.query_params.clear()
                st.rerun()
            else:
                st.error(f"Login failed: {res.text}")
        except Exception as e:
            st.error(f"Login error: {e}")
    else:
        login_url = (
            f"{COGNITO_DOMAIN}/login?"
            f"client_id={CLIENT_ID}&"
            f"response_type=code&"
            f"scope=email+openid+phone&"
            f"redirect_uri={REDIRECT_URI}&"
            f"state=xyz&"
            f"persona={persona}"
        )
        st.markdown(f"[Login with Google SSO]({login_url}&persona={st.session_state['persona']})")

