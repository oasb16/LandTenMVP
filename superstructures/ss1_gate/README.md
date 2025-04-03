# Hybrid SS1_Gate Enhanced

## Overview
This module handles Google SSO login via AWS Cognito with persona-aware signup and DynamoDB write support.

## Run Instructions

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Start Flask backend:
```
cd flask_backend
python ss1_backend.py
```

3. Run Streamlit frontend:
```
cd streamlit_frontend
streamlit run ss1_gate_app.py
```

4. Login options:
- Sign In: http://localhost:5000/signin
- Sign Up (Tenant): http://localhost:5000/signup?persona=tenant
- Sign Up (Landlord): http://localhost:5000/signup?persona=landlord
- Sign Up (Contractor): http://localhost:5000/signup?persona=contractor
