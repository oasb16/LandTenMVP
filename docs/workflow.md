
# 🧭 LandTen MVP Workflow Overview

This document outlines the current system architecture and end-to-end persona-based flow for the LandTen MVP.

---

## 🔐 SS1: Gate – AWS Cognito Authentication
- Users log in via Google SSO
- AWS Cognito captures user email and persona (via query param)
- DynamoDB stores identity mapping for persona routing

---

## 📊 SS2: Pulse – Persona-Based Dashboard Router
- Streamlit sidebar radio allows selection of tenant, landlord, contractor, or admin
- `streamlit_app.py` dynamically loads relevant interface per persona
- Admin view triggers the protocol tracker dashboard

---

## 🧠 SS3: Echo – Tenant GPT Chat + Incident Summary
- GPT-powered 5-turn, 20-word-max chat interface
- Summarizes issue into structured incident format
- Generates incident ID, summary, keywords, priority, contractor type, charge estimate
- Stores structured data in `incident_table` (DynamoDB or similar)

---

## 🔁 SS4: Root – Incident Queue Middleware
- Ensures atomic queueing of incidents
- Uses AWS SQS with deduplication
- Queued incidents forwarded to landlord dashboard

---

## 🧾 SS5: View – Landlord Incident Dashboard
- Landlord sees incident summaries
- Can escalate into job tickets
- Includes filtering by priority, category, contractor type

---

## 🎟 SS6: Cast – Contractor Ticket Creation
- Converts incident into job ticket
- Supports identity validation, license attachment
- Initiates bid flow or direct assignment

---

## 🔗 SS7: Bind – Contractor Response + Ledger
- Contractor views and responds to assigned job
- Ledger initiated for job tracking
- Accept, reject, or propose alternate terms

---

## 📅 SS8: Sync – Scheduling Interface
- Landlord and contractor negotiate job schedule
- GPT used to summarize scheduling options
- Timestamped confirmation stored in ledger

---

## ✅ SS9: Seal – Completion & Verification
- Job marked complete by contractor
- Landlord/tenant verifies via:
  - Photo upload
  - Written notes
  - Verbal voice clip
- Contractor uploads receipt

---

## 💳 SS10: Core – Streamlit Shell + Payment Placeholder
- Master shell interface in Streamlit
- Prepares for integration with payment gateway (Stripe, etc.)
- Dashboard includes job status, payment triggers

---

## 🗂 Tracker: Protocol Status Monitor
- Live status of all superstructures
- `landten_protocol_tracker_app.py` renders dashboard
- Pulls `.status` and timestamp from each SS folder

---

## 🚧 Notes
- GPT summarization modules reuse common interface
- All persona workflows route through unified Streamlit shell
- Errors and logging built into each superstructure progressively

