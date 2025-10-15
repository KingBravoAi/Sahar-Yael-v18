backend/app/embodiment/homeostasis.py (DSL stub)
# Digital Pheromones DSL: "signal: level -> effect"
# Example: "cortisol: 0.8 -> throttle.fusion.fanout=3"
import re

ASSIGN = re.compile(r"^\s*([a-z_]+)\s*:\s*([0-1](?:\.\d+)?)\s*->\s*([a-z\.]+)\s*=\s*([0-9\.]+)\s*$")

def apply_rule(rule:str, runtime_cfg:dict)->dict:
    m = ASSIGN.match(rule)
    if not m: return runtime_cfg
    signal, level, target, value = m.group(1), float(m.group(2)), m.group(3), float(m.group(4))
    # simple policy: only apply if level >= 0.7
    if level >= 0.7:
        # navigate dotted path in runtime_cfg
        node = runtime_cfg
        parts = target.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p,{})
        node[parts[-1]] = value
    return runtime_cfg

(Other stubs—aperture.py, actuator.py, metabolic.py—can stay minimal for MVP; you can expand as needed.)
