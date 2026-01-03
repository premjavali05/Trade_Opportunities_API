from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

VALID_TOKENS = {
    "demo-token": "demo-user"
}

def verify_token(
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    token = credentials.credentials

    if token not in VALID_TOKENS:
        raise HTTPException(status_code=401, detail="Invalid token")

    return VALID_TOKENS[token]
