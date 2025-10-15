backend/app/api/routes.py
from fastapi import APIRouter
from .schemas import *
from ..mastery.v9r import compute_overall
from ..quantum.engine import score_strategy
from ..fusion.routing import run_fusion
from ..quantum.forest import run_forest
from ..provenance.manifest import manifest_for

router = APIRouter()

@router.post("/score", response_model=ScoreResp)
def score(req: ScoreReq):
    overall, detail = compute_overall(req.profile, req.pillars)
    m = manifest_for("score", inputs=req.model_dump(), outputs={"overall":overall,"detail":detail})
    return {"overall":overall,"detail":detail,"manifest":m}

@router.post("/quantum/explore", response_model=QuantumResp)
def explore(req: QuantumReq):
    scores = [score_strategy(s) for s in req.strategies]
    best = max(range(len(scores)), key=lambda i: scores[i])
    m = manifest_for("quantum/explore", inputs=req.model_dump(), outputs={"scores":scores,"best_index":best})
    return {"scores":scores,"best_index":best,"manifest":m}

@router.post("/fusion/complete", response_model=FusionResp)
def fusion(req: FusionReq):
    steps, collapsed = run_fusion(req.task, req.subtasks, req.models, req.constraints)
    m = manifest_for("fusion/complete", inputs=req.model_dump(), outputs={"steps":steps,"collapsed":collapsed})
    return {"steps":steps,"collapsed":collapsed,"manifest":m}

@router.post("/forest/run", response_model=ForestResp)
def forest(req: ForestReq):
    branches, collapsed, metrics = run_forest(req.task, req.fanout, req.keep_top_n)
    m = manifest_for("forest/run", inputs=req.model_dump(), outputs={"branches":branches,"collapsed":collapsed,"metrics":metrics})
    return {"branches":branches,"collapsed":collapsed,"metrics":metrics,"manifest":m}

@router.post("/manifests/graph/query")
def graph_query(req: GraphQueryReq):
    # stub: return empty
    return {"rows":[]}
