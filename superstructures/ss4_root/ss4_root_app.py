from validator import validate_incident
from queue_stub import enqueue_incident
from file_writer import write_status_and_log
import os, json

def run_root_ingestion():
    QUEUE_PATH = "queue/"
    os.makedirs(QUEUE_PATH, exist_ok=True)

    for fname in os.listdir(QUEUE_PATH):
        if fname.endswith(".json") and not fname.endswith(".status.json"):
            with open(os.path.join(QUEUE_PATH, fname)) as f:
                data = json.load(f)
            try:
                incident = validate_incident(data)
                enqueue_incident(incident, QUEUE_PATH)
                write_status_and_log(incident, QUEUE_PATH)
                print(f"Ingested: {incident.interaction_id}")
            except Exception as e:
                print(f"Validation failed for {fname}: {e}")
