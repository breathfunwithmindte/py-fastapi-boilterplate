from fastapi import FastAPI, Body

from microservices.auth.middleware import PrimaryMicroserviceMiddleware
from config import settings

from microservices.primary.routers.v1.article import article_router


primary_microservice = FastAPI(
    title=settings.PRIMARY_TITLE,
    description=settings.PRIMARY_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
)

# ADD MIDDLEWARES
primary_microservice.add_middleware(middleware_class=PrimaryMicroserviceMiddleware)

# INCLUDE ROUTES FOR CURRENT MICRO SERVICE
primary_microservice.include_router(article_router, prefix="/article")

@primary_microservice.get("/test-api/{username}")
def admin_test_api (username: str):
    return { "message": f"Hello, {username}" }