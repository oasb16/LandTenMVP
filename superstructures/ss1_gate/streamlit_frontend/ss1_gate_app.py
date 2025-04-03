import streamlit as st
import requests
import base64
import json
from datetime import datetime
import jwt
from urllib.parse import quote, unquote
from superstructures.ss1_gate.persona_extractor import extract_persona
from superstructures.ss1_gate.shared.dynamodb import write_user_profile

# Configuration
CLIENT_ID = st.secrets.get("COGNITO_CLIENT_ID")
COGNITO_CLIENT_SECRET = st.secrets.get("COGNITO_CLIENT_SECRET")
COGNITO_DOMAIN = "https://us-east-1liycxnadt.auth.us-east-1.amazoncognito.com"
REDIRECT_URI = "https://landtenmvpmainapp.streamlit.app/"
TOKEN_ENDPOINT = f"{COGNITO_DOMAIN}/oauth2/token"

def run_login():
    # Let user pick role if not set yet
    if "persona" not in st.session_state:
        st.session_state["persona"] = st.selectbox("Choose your role", ["tenant", "landlord", "contractor"])

    query_params = st.query_params
    code = query_params.get("code", None)
    state_raw = query_params.get("state", None)

    # Decode persona from state param
    try:
        decoded_state = json.loads(unquote(state_raw)) if state_raw else {}
        persona = decoded_state.get("persona", st.session_state.get("persona", "tenant"))
    except:
        persona = st.session_state.get("persona", "tenant")

    if code:
        # Prevent reusing same code
        if "last_code" in st.session_state and st.session_state["last_code"] == code:
            st.warning("⚠️ Duplicate login attempt — please refresh and retry.")
            return
        st.session_state["last_code"] = code

        # Basic Auth header
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

                # Set session
                st.session_state["logged_in"] = True
                st.session_state["email"] = user_info.get("email", "")
                st.session_state["persona"] = persona

                # Write to DB
                try:
                    write_user_profile({
                        "email": st.session_state["email"],
                        "persona": persona,
                        "login_source": "GoogleSSO",
                        "timestamp": datetime.utcnow().isoformat()
                    })
                    st.success(f"✅ Profile saved to DynamoDB for {persona}: {st.session_state['email']}")
                except Exception as db_err:
                    st.error(f"❌ Failed to write user to DB: {db_err}")

                # Clean URL and rerun
                st.query_params.clear()
                st.rerun()
            else:
                st.error(f"Login failed: {res.text}")
        except Exception as e:
            st.error(f"Login error: {e}")
    else:
        # Encode persona in OAuth state param
        state_json = json.dumps({"persona": st.session_state["persona"]})
        encoded_state = quote(state_json)

        login_url = (
            f"{COGNITO_DOMAIN}/login?"
            f"client_id={CLIENT_ID}&"
            f"response_type=code&"
            f"scope=email+openid+phone&"
            f"redirect_uri={REDIRECT_URI}&"
            f"state={encoded_state}"
        )
        st.markdown(f"[🔐 Login with Google SSO]({login_url})")
