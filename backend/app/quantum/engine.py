backend/app/quantum/engine.py
def clip(x,lo=0,hi=1): return max(lo,min(hi,x))
def score_strategy(s:dict)->float:
    impact = clip(s["impact"]); ttv = clip(s["time_to_value"])
    risk = clip(1.0 - s["risk"]); cplx = clip(1.0 - s["complexity"])
    return 0.40*impact + 0.25*ttv + 0.20*risk + 0.15*cplx

