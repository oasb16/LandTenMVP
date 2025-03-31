
import streamlit as st
import pandas as pd

st.set_page_config(page_title="LandTen Protocol Tracker", layout="wide")
st.title("🗂 LandTen MVP Protocol Tracker")

data = {
    "Protocol": ["Gate", "Pulse", "Echo", "Root", "View", "Cast", "Bind", "Sync", "Seal", "Core"],
    "Superstructure": [
        "SS1: AWS Cognito Authentication",
        "SS2: Persona-Based Dashboard Router",
        "SS3: Tenant GPT Chat + Incident Summary",
        "SS4: Incident Queue Middleware",
        "SS5: Landlord Incident Dashboard",
        "SS6: Contractor Ticket Creation",
        "SS7: Contractor Response + Ledger",
        "SS8: Scheduling Interface",
        "SS9: Completion & Verification",
        "SS10: Streamlit Shell + Payment Placeholder"
    ],
    "Status": [
        "zipped", "zipped", "in-dev", "waiting", "waiting",
        "waiting", "waiting", "waiting", "waiting", "scaffolded"
    ],
    "Output_Link": [
        "[ZIP_Gate]", "[ZIP_Pulse]", "-", "-", "-", "-", "-", "-", "-", "-"
    ],
    "Integration_Ready": ["✅", "✅", "❌", "❌", "❌", "❌", "❌", "❌", "❌", "❌"],
    "Last_Updated": ["2025-03-31"] * 10,
    "Notes": [
        "Persona saved in DynamoDB", "Routing by persona tested", "GPT not yet connected",
        "Waiting for incident output", "UI layout needed", "Contractor type matcher not wired",
        "Bid interaction logic to be built", "Needs calendar logic",
        "Photo/text confirmation path TBD", "Streamlit app shell exists"
    ]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

st.success("🗂 LandTen MVP Main Github : https://github.com/oasb16/LandTenMVP")
st.success("🗂 LandTen MVP Playbook : https://github.com/oasb16/LandTenMVP/blob/master/docs/LandTen_Playbook.md")
st.success("🗂 LandTen MVP Manifesto: https://github.com/oasb16/LandTenMVP/blob/master/docs/LandTen_Manifesto.md")
st.success("🗂 LandTen MVP Tracker: https://github.com/oasb16/LandTenMVP/blob/master/protocol_tracker/landten_protocol_tracker_app.py")
