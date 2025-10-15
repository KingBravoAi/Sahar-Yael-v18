backend/app/api/schemas.py
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class ScoreReq(BaseModel):
    profile: str = Field("Human-Broad")
    pillars: Dict[str, float]

class ScoreResp(BaseModel):
    overall: float
    detail: Dict[str, float]
    manifest: Dict[str, object]

class QuantumReq(BaseModel):
    strategies: List[Dict[str,float]]

class QuantumResp(BaseModel):
    scores: List[float]
    best_index: int
    manifest: Dict[str, object]

class FusionReq(BaseModel):
    task: str
    subtasks: Optional[List[str]] = None
    models: Dict[str, str] = {"reasoner":"grok4","polisher":"gpt5","executor":"local"}
    constraints: Dict[str, float] = {"max_tokens":512, "cost_ceiling_usd":0.05}

class FusionResp(BaseModel):
    steps: List[Dict[str, object]]
    collapsed: Dict[str, object]
    manifest: Dict[str, object]

class ForestReq(BaseModel):
    task: str
    fanout: int = 8
    keep_top_n: int = 3

class ForestResp(BaseModel):
    branches: List[Dict[str, object]]
    collapsed: Dict[str, object]
    metrics: Dict[str, object]
    manifest: Dict[str, object]

class GraphQueryReq(BaseModel):
    cypher: str
