from jsonschema import validate
from pydantic import BaseModel, ValidationError, field_validator, field_serializer
from models.triage_agent import ReportSchema



from pydantic import ValidationError
import json

# Example input data
input_data = {
    "report_id": "2024-07-18-001",
    "AOI": True,
    "IOC": True,
    "CVSS": 8.7,
    "APT": ["APT28", "APT29"],
    "Confidence": {
        "p_value": 85.0,
        "description": "High confidence level"
    },
    "mitre_id": ["T1059", "T1071"],
    "LLM_Approved": False,
    "distribution": ["Internal", "Partners"],
    "content": {
        "summary": "An advanced persistent threat (APT) group, identified as APT28 and APT29, has been observed conducting sophisticated attacks against critical infrastructure.",
        "detailed_description": "The attackers leveraged spear-phishing campaigns and zero-day exploits to gain initial access. They used T1059 for command and scripting interpreter and T1071 for application layer protocols to exfiltrate data.",
        "indicators_of_compromise": ["192.168.1.100", "malicious.com", "filehash1234567890abcdef"],
        "recommended_actions": ["Patch vulnerable systems", "Implement network segmentation", "Enhance monitoring and incident response capabilities"]
    },
    "previous_party": "Initial Analyst",
    "chain_of_custody": ["Initial Analyst"],
    "created_at": "2024-07-18T12:34:56Z",
    "updated_at": "2024-07-18T12:34:56Z"
}

try:
    report = ReportSchema(**input_data)
    # Coerced JSON output
    report_json = report.json(indent=2)
    print(report_json)
except ValidationError as e:
    print("Validation error:", e.json(indent=2))
