backend/app/main.py
from fastapi import FastAPI, Depends, Header, HTTPException
from .api.routes import router as api_router
from .deps import require_key

app = FastAPI(title="Sahar Yael v18 MVP")

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/version")
def version():
    return {"version": "V18.0.0", "weights_version": "v14.0.1"}

app.include_router(api_router, dependencies=[Depends(require_key)])
