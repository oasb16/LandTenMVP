import os
import datetime

def update_status(path: str, status: str):
    timestamp = datetime.datetime.utcnow().isoformat()
    with open(path, "w") as f:
        f.write(f"{status}|{timestamp}")

def read_status(path: str):
    if not os.path.exists(path):
        return "missing", None
    with open(path) as f:
        parts = f.read().strip().split("|")
        status = parts[0]
        timestamp = parts[1] if len(parts) > 1 else None
        return status, timestamp