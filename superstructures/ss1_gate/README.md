# SS1_Gate — Streamlit-Only AWS Cognito Login

## Overview
This superstructure enables AWS Cognito + Google SSO login via hosted UI, completely managed within Streamlit (no Flask).

## Flow
1. User hits app with query param `?persona=contractor`
2. Streamlit builds Cognito login URL → redirects to Google SSO
3. Cognito redirects back to Streamlit with `?code=`
4. Code is exchanged for tokens
5. `st.session_state` is populated:
```python
{
  "email": "xyz@example.com",
  "persona": "contractor",
  "logged_in": True
}
```

## Setup
1. Configure your `.env`:
```
COGNITO_CLIENT_ID=
COGNITO_DOMAIN=your-domain.auth.us-east-1.amazoncognito.com
REDIRECT_URI=https://your-app-url/
```

2. Add to `streamlit_app.py`:
```python
from superstructures.ss1_gate.ss1_gate_app import run_login

if "logged_in" not in st.session_state:
    run_login()
    st.stop()
```

3. After login, call:
```python
from superstructures.ss2_pulse.ss2_pulse_app import run_router
run_router()
```
