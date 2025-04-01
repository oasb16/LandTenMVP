from contracts.ss3_echo_contract import IncidentInput

def validate_incident(data):
    return IncidentInput(**data)
