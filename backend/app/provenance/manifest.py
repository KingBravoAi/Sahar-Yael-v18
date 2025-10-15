backend/app/provenance/manifest.py
import json, hashlib, time, os

def hash_obj(obj)->str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",",":")).encode()).hexdigest()

def manifest_for(endpoint:str, inputs:dict, outputs:dict)->dict:
    m = {
        "run_id": f"{endpoint}-{int(time.time()*1000)}",
        "endpoint": endpoint,
        "inputs": inputs,
        "outputs": outputs,
        "adapter_meta": {"provider": os.getenv("SY_MODEL_PROVIDER","local")},
        "governance_meta": {"weights_version": "v14.0.1"},
        "cost_meta": {"usd_estimate": 0.005},
        "timestamps": {"created_at": time.time()}
    }
    m["sha256_hash"] = hash_obj(m)
    return m

