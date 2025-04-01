# 🔁 SS4_Root (Incident Queue Middleware)

Middleware for ingesting validated incident summaries from SS3_Echo.
Performs validation, deduplication, and dispatch via stubbed file queue or SQS.

## ✅ Functions
- Validate using `contracts.ss3_echo_contract.IncidentInput`
- Deduplicate using `interaction_id`
- Write `.incident`, `.status`, and `.log` files to `queue/`
