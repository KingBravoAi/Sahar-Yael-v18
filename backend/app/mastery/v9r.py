backend/app/mastery/v9r.py
import math

WEIGHTS = {"IQ":0.24,"EQ":0.20,"CQ":0.22,"AQ":0.18,"Vision":0.16}
def clip(x, lo=0.0, hi=1.0): return max(lo, min(hi, x))
def pvar(xs):
    n=len(xs); m=sum(xs)/n; return sum((x-m)**2 for x in xs)/n
def sigmoid(x): return 1.0/(1.0+math.exp(-6.0*(x-0.5)))

def compute_overall(profile:str, pillars:dict):
    bounds = {"Human-Broad":(30.0,140.0),"Human-Scale":(50.0,150.0),"Superhuman":(0.0,200.0)}
    lo,hi = bounds.get(profile, bounds["Human-Broad"])
    norms = {k:clip((pillars[k]-lo)/(hi-lo)) for k in WEIGHTS}
    core = sum(WEIGHTS[k]*norms[k] for k in WEIGHTS)
    var = pvar(list(norms.values()))
    cohesion = clip(1.0 - math.sqrt(var*10.0),0,1)          # sqrt cohesion
    synergy = 0.20 * core * cohesion
    imbalance = 0.15 * (max(norms.values()) - min(norms.values()))
    sig = sigmoid(core)
    nl = 0.06 * max(0.0, sig - core)
    overall = 100.0 * clip(core + synergy - imbalance + nl, 0, 1)
    detail = {"core":core,"cohesion":cohesion,"synergy":synergy,"imbalance":imbalance,"sigmoid":sig,"nonlinear":nl}
    return overall, detail
