backend/app/deps.py
import os
from fastapi import Header, HTTPException

API_KEY = os.getenv("API_KEY","dev-key")
def require_key(x_api_key: str = Header(default="dev-key")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

