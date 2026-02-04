from fastapi import FastAPI, Request, HTTPException
import base64
import json

app = FastAPI()

def get_user_from_headers(request: Request):
    principal = request.headers.get("x-ms-client-principal")
    if not principal:
        raise HTTPException(status_code=401, detail="Not authenticated")

    decoded = base64.b64decode(principal)
    user = json.loads(decoded)
    return user

@app.get("/")
async def hello(request: Request):
    user = get_user_from_headers(request)
    return {
        "message": "Hello world",
        "user": {
            "name": user.get("name"),
            "email": user.get("preferred_username"),
            "oid": user.get("oid"),
            "tenant": user.get("tid")
        }
    }
