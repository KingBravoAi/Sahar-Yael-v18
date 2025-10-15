backend/app/fusion/routing.py
def run_fusion(task:str, subtasks, models, constraints):
    # autosplit
    st = subtasks or ["plan","draft","refine"]
    steps=[]
    # mock steps per role
    for role in ["reasoner","polisher","executor"]:
        steps.append({
            "role": role,
            "subtask": f"{st[0]}: {task}",
            "adapter": models.get(role,"local"),
            "usage": {"tokens_in":120,"tokens_out":200,"est_cost_usd":0.005},
            "output": f"{role} output for '{task}'"
        })
    collapsed = {"rationale":"selected executor output (score:0.85)","output":f"Final: {task} plan","score":0.85}
    return steps, collapsed

