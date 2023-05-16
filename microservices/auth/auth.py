from fastapi import FastAPI, Body

from microservices.auth.middleware import PrimaryMicroserviceMiddleware
from config import settings

from microservices.auth.routers.v1.jwt_authentication import jwt_authentication_router


auth_microservice = FastAPI(
    title=settings.ADMIN_TITLE,
    description=settings.ADMIN_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
)

# ADD MIDDLEWARES
auth_microservice.add_middleware(middleware_class=PrimaryMicroserviceMiddleware)

# INCLUDE ROUTES FOR CURRENT MICRO SERVICE
auth_microservice.include_router(jwt_authentication_router, prefix="/jwt-auth")

@auth_microservice.get("/test-api/{username}")
def admin_test_api (username: str):
    return { "message": f"Hello, {username}" }