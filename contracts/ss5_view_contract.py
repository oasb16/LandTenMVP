from pydantic import BaseModel
from typing import List

class IncidentInput(BaseModel):
    interaction_id: str
    summary: str
    keywords: List[str]
    priority: str
    contractor_type: str
    contractor_summary: str