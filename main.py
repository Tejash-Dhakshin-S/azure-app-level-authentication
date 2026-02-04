from fastapi import FastAPI, Request, HTTPException
import base64, json

app = FastAPI()

def get_user(request: Request):
    principal = request.headers.get("x-ms-client-principal")
    if not principal:
        raise HTTPException(status_code=401)

    decoded = base64.b64decode(principal)
    data = json.loads(decoded)

    claims = {c["typ"]: c["val"] for c in data.get("claims", [])}

    return {
        "name": claims.get("name"),
        "email": claims.get("preferred_username"),
        "oid": claims.get("oid"),
        "tenant": claims.get("tid")
    }

@app.get("/")
async def hello(request: Request):
    user = get_user(request)
    return {
        "message": "Hello world",
        "user": user
    }
