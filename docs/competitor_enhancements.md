# 🧠 Competitor-Inspired Enhancements for LandTen MVP

_Last updated: 2025-04-01_

This document outlines enhancement opportunities inspired by features in competitor apps like **TurboTenant** and **Lula**, along with analysis on MVP inclusion, development cost, token/GPT usage impact, and strategic justification.

---

## ✅ Enhancement Opportunities (NOT MVP-Blockers)

| Feature | Recommendation |
|--------|----------------|
| **Real Estate Attorney Role** | Defer to post-MVP or bundle under `admin` persona. |
| **Invite Contractor + Verify Identity** | Bundle into SS6 `Cast` as an onboarding wizard. |
| **HOA Issues for Tenants** | Add `"hoa_dispute"` to `issue_category` enum (SS3), but not mandatory. |
| **Legal Advice / Documents** | Optional via admin interface in future versions. |
| **OAuth (Facebook/Apple)** | Supported via AWS Cognito; enable post-MVP. |

---

## 📊 Cost Impact & Metric Shift Table

| Feature | Source App | MVP Inclusion | 💰 Cost Drivers | 📈 Impact if Added to MVP |
|--------|-------------|----------------|------------------|-----------------------------|
| **GPT-threaded Issue History** | TurboTenant | ❌ Post-MVP | - Chat history storage (DynamoDB/S3)<br>- GPT summary token cost<br>- Thread versioning logic | 🔼 Token usage/cost<br>🔼 Dev complexity (SS4/SS9)<br>✅ +20% tenant trust & engagement |
| **Legal Notice Auto-Fill via GPT** | TurboTenant | ❌ Post-MVP | - Prompt engineering<br>- Document version control<br>- Legal liability & review overhead | 🔼 API token cost<br>🔼 Legal validation required<br>✅ +10% perceived professionalism |
| **Contractor Onboarding + License Check** | Lula | ✅ MVP via SS6 | - Wizard UI<br>- Enum + file upload<br>- License type mapping | 🟢 Easy to implement<br>✅ +15% bid quality/trust |
| **Real-Time Scheduling & GPT Chat Summary** | Lula, Turbo | ❌ Post-MVP | - WebSocket/polling infra<br>- GPT thread summarization<br>- Timestamping & notification | 🔼 Backend infra & API cost<br>✅ +25% scheduling success<br>✅ Liability log benefit |
| **Landlord Metric Dashboard** | Lula, Turbo | ❌ Post-MVP | - Log aggregation<br>- UI visualizations<br>- Incident analytics (ML optional) | 🔼 3–5 dev days<br>✅ +18% landlord retention |

---

## 🧮 Breakdown of Cost Drivers

| Driver | Description | Cost Type |
|--------|-------------|-----------|
| 🧠 **GPT Token Usage** | GPT-4o calls for chat summaries, document generation | Variable / Monthly |
| 📦 **Data Storage** | S3/DynamoDB for chat threads, uploads, logs | Free tier → scalable |
| 📈 **Charts & Dashboards** | Incident stats, filters, ML contractor ranks | Dev + Charting libs |
| 🔄 **Session Context** | Persistent threads for users/landlords | Logic overhead |
| 🔁 **Real-time Infra** | Live scheduling/chat | Highest cost unless stubbed |

---

## 🎯 MVP Inclusion Recommendation

Only the following enhancement should be bundled into MVP:
- ✅ **Contractor Onboarding + License Check**: valuable trust signal, low-cost, fits SS6 cleanly.

All other features should be deferred until post-MVP when monetization and usage patterns justify expansion.

---

## 📌 Next Steps

- [ ] Implement contractor onboarding wizard in SS6 `Cast`
- [ ] Create stubs or enums for `hoa_dispute`, legal doc types
- [ ] Track GPT-token usage post-MVP for feasibility review

