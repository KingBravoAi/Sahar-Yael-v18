backend/app/quantum/forest.py
import random
from .engine import score_strategy

def run_forest(task:str, fanout:int=8, keep_top_n:int=3):
    # toy generator: synthesize strategies from task hash
    random.seed(hash(task) & 0xffffffff)
    branches=[]
    for i in range(fanout):
        s = {"impact":random.random(),"time_to_value":random.random(),
             "risk":random.random(),"complexity":random.random()}
        branches.append({"i":i,"strategy":s,"score":score_strategy(s)})
    branches.sort(key=lambda b: b["score"], reverse=True)
    top = branches[:keep_top_n]
    collapsed = {"choice": top[0], "rationale": "argmax score"}
    metrics = {"forest_branches_evaluated": fanout}
    return branches, collapsed, metrics
