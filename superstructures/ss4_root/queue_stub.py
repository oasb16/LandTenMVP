import json
import os

def enqueue_incident(incident, base_path):
    path = os.path.join(base_path, f"{incident.interaction_id}.incident.json")
    if not os.path.exists(path):
        enriched = incident.dict()
        enriched["status"] = "ticket_created"
        enriched["origin"] = "ss3_echo"
        enriched["ingested_at"] = __import__('datetime').datetime.utcnow().isoformat()
        with open(path, "w") as f:
            json.dump(enriched, f, indent=2)
