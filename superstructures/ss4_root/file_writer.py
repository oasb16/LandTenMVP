import os
from datetime import datetime

def write_status_and_log(incident, base_path):
    status_file = os.path.join(base_path, f"{incident.interaction_id}.status.json")
    log_file = os.path.join(base_path, f"{incident.interaction_id}.log.txt")
    
    with open(status_file, "w") as sf:
        sf.write('{"status": "ticket_created"}')
    
    with open(log_file, "a") as lf:
        lf.write(f"[{datetime.utcnow().isoformat()}] Ingested from ss3_echo\n")
