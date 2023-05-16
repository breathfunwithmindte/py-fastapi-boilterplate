from fastapi import Request
from core.exceptions import ForbiddenException, NonAuthenticatedException

# namespace ~> microservices::auth::dependencies.py

# short middleware that can be used instead of primary Middleware.
def passport (req: Request):
    if req.headers.get("authorization") is None: raise NonAuthenticatedException()
    # do something like verify the token
    req.state.user = { "username": "@Mike", "role": "admin" }
    
def admin_only (req: Request):
    if req.state.user["role"] is not "admin":
        raise ForbiddenException()