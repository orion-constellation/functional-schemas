from typing import List, Optional
from pydantic import BaseModel, Field, UUID4, field_validator
from datetime import datetime

class Confidence(BaseModel):
    p_value: float = Field(..., ge=0.0, le=100.0, description="Confidence percentage")
    description: str = Field(..., description="Description of the confidence level")

    @field_validator('p_value')
    def check_confidence(cls, v):
        if v < 80.0:
            raise ValueError('Confidence level must be at least 80%')
        return v

class Content(BaseModel):
    summary: str = Field(..., description="Brief summary of the threat")
    detailed_description: str = Field(..., description="Detailed description of the threat and activities observed")
    indicators_of_compromise: List[str] = Field(..., description="List of indicators of compromise")
    recommended_actions: List[str] = Field(..., description="Recommended actions to mitigate the threat")

class ReportSchema(BaseModel):
    report_id: str = Field(..., description="Unique identifier for the intelligence report")
    AOI: bool = Field(..., description="Area of interest")
    IOC: bool = Field(..., description="Indicator of compromise present")
    CVSS: float = Field(..., ge=0.0, le=10.0, description="Common Vulnerability Scoring System score")
    APT: List[str] = Field(..., description="Advanced Persistent Threat groups involved")
    Confidence: Confidence = Field(..., description="Confidence level of the report's findings")
    mitre_id: List[str] = Field(..., description="MITRE ATT&CK technique IDs")
    LLM_Approved: bool = Field(..., description="Approval status by a large language model or automated system")
    distribution: List[str] = Field(..., description="Distribution list for the report")
    content: Content = Field(..., description="Detailed content of the report")
    previous_party: str = Field(..., description="Entity that handled the report before the current party")
    chain_of_custody: List[str] = Field(..., description="Chain of custody for the report")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Datetime when the report was created")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Datetime when the report was last updated")

    @field_validator('chain_of_custody')
    def check_chain_of_custody(cls, v, values):
        if 'previous_party' in values and values['previous_party'] not in v:
            raise ValueError('previous_party must be part of chain_of_custody')
        return v
