import streamlit as st
import pandas as pd
import os
from utils.status_tracker import read_status

st.set_page_config(page_title="LandTen MVP Protocol Tracker", layout="wide")
st.title("🗂 LandTen MVP Protocol Tracker")

superstructures = [
    ("Gate", "SS1: AWS Cognito Authentication", "ss1_gate"),
    ("Pulse", "SS2: Persona-Based Dashboard Router", "ss2_pulse"),
    ("Echo", "SS3: Tenant GPT Chat + Incident Summary", "ss3_echo"),
    ("Root", "SS4: Incident Queue Middleware", "ss4_root"),
    ("View", "SS5: Landlord Incident Dashboard", "ss5_view"),
    ("Cast", "SS6: Contractor Ticket Creation", "ss6_cast"),
    ("Bind", "SS7: Contractor Response + Ledger", "ss7_bind"),
    ("Sync", "SS8: Scheduling Interface", "ss8_sync"),
    ("Seal", "SS9: Completion & Verification", "ss9_seal"),
    ("Core", "SS10: Streamlit Shell + Payment Placeholder", "ss10_core"),
]

statuses = []
timestamps = []

for _, _, folder in superstructures:
    path = f"../superstructures/{folder}/.status"
    status, ts = read_status(path)
    statuses.append(status)
    timestamps.append(ts or "-")

df = pd.DataFrame({
    "Protocol": [x[0] for x in superstructures],
    "Superstructure": [x[1] for x in superstructures],
    "Status": statuses,
    "Last Updated": timestamps,
})

st.dataframe(df, use_container_width=True)