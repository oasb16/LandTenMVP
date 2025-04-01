# 🧠 LandTen Enhancement Opportunities (Non-MVP Blockers)

This document outlines strategic feature enhancements identified during the MVP design phase. These are **not required for the MVP**, but are valuable additions for improving system robustness, user experience, and legal/operational compliance in future releases.

---

## 🔒 Real Estate Attorney Role

- **Description:** Add a specialized persona for real estate attorneys to review legal issues, interpret lease terms, or mediate disputes.
- **Recommendation:** Defer to post-MVP. In early stages, consider bundling this role into the existing `admin` persona for prototyping purposes.

---

## 🛠️ Invite Contractor + Identity Verification

- **Description:** Allow landlords/admins to invite external contractors by email/SMS and verify their identity using basic KYC (e.g., ID upload or contractor license).
- **Recommendation:** Bundle into `SS6: Cast` during or after MVP. Consider using AWS Cognito for identity validation.

---

## 🏢 HOA Issue Tagging for Tenants

- **Description:** Tenants may report HOA-related issues that require routing to homeowner associations, not landlords.
- **Recommendation:** Add `"HOA"` to the `issue_category` enum list in incident submission form. Implement actual HOA routing post-MVP.

---

## 📄 Legal Advice / Document Upload

- **Description:** Provide tenants and landlords with template legal documents, lease interpretation, or a GPT-backed legal FAQ.
- **Recommendation:** Optional under the `admin` persona. Could be powered by GPT-4o or external legal APIs in future releases.

---

## 🔑 OAuth via Facebook / Apple / etc.

- **Description:** Provide additional sign-in methods beyond Google.
- **Recommendation:** AWS Cognito natively supports multiple federated identity providers. Post-MVP, enable Facebook, Apple, LinkedIn login with minimal config updates.

---

## 📌 Summary Table

| Feature                             | Recommendation                              |
|-------------------------------------|----------------------------------------------|
| Real estate attorney role           | Push to post-MVP / bundle into admin         |
| Invite contractor + verify identity| Bundle into SS6: Cast                        |
| HOA issues for tenants              | Add to issue_category enum                   |
| Legal advice / documents            | Optional under admin persona                 |
| OAuth via Facebook/Apple/etc        | Supported by Cognito — implement post-MVP    |

---
