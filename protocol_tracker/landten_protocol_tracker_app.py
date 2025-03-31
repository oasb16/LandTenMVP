
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="LandTen MVP Protocol Tracker", layout="wide")
st.title("🗂 LandTen MVP Protocol Tracker")

# Mapping superstructure protocols
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

base_path = "../superstructures"
statuses = []
output_links = []
integration_ready = []
notes = []

for protocol, description, folder in superstructures:
    status_path = os.path.join(base_path, folder, ".status")
    if os.path.exists(status_path):
        with open(status_path) as f:
            status = f.read().strip()
    else:
        status = "missing"

    statuses.append(status)
    output_links.append("ZIP" if status in ["zipped", "integrated"] else "-")
    integration_ready.append("✅" if status in ["tested", "integrated"] else "❌")
    notes.append("Auto-read from .status file")

# Build DataFrame
df = pd.DataFrame({
    "Protocol": [x[0] for x in superstructures],
    "Superstructure": [x[1] for x in superstructures],
    "Status": statuses,
    "Output_Link": output_links,
    "Integration_Ready": integration_ready,
    "Notes": notes
})

st.dataframe(df, use_container_width=True)


st.success("🗂 LandTen MVP Main Github : https://github.com/oasb16/LandTenMVP")
st.success("🗂 LandTen MVP Playbook : https://github.com/oasb16/LandTenMVP/blob/master/docs/LandTen_Playbook.md")
st.success("🗂 LandTen MVP Manifesto: https://github.com/oasb16/LandTenMVP/blob/master/docs/LandTen_Manifesto.md")
st.success("🗂 LandTen MVP Tracker: https://github.com/oasb16/LandTenMVP/blob/master/protocol_tracker/landten_protocol_tracker_app.py")
