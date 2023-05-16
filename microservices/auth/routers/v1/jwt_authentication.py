from fastapi import APIRouter, Request, Depends
from core.exceptions import *
from core.utils import *
from microservices.auth.dependencies import *
from microservices.auth.schema.AuthLoginRequest import AuthLoginRequest
from microservices.auth.schema.AuthRegisterRequest import AuthRegisterRequest
from config import settings

# namespace ~> microservices::auth::routers::v1::jwt_authentication

jwt_authentication_router = APIRouter() # include _router at the end of the name.


#
# Add comments here
#
@jwt_authentication_router.post("/login", dependencies=[])
async def login (req: Request, loginBody: AuthLoginRequest):
    return {
        "message": "Login api require implemetation",
        "data": loginBody
    }



#
# Add comments here
#
@jwt_authentication_router.post("/register", dependencies=[])
async def register (req: Request, registerBody: AuthRegisterRequest):
    return {
        "message": "Register api require implemetation",
        "data": registerBody
    }