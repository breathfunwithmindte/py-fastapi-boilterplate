from fastapi import FastAPI, Body

from microservices.admin.middleware import PrimaryMicroserviceMiddleware
from config import settings

from microservices.admin.routers.v1.application_setting import application_setting_router


admin_microservice = FastAPI(
    title=settings.ADMIN_TITLE,
    description=settings.ADMIN_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
)

# ADD MIDDLEWARES
admin_microservice.add_middleware(middleware_class=PrimaryMicroserviceMiddleware)

# INCLUDE ROUTES FOR CURRENT MICRO SERVICE
admin_microservice.include_router(application_setting_router, prefix="/app.do")

@admin_microservice.get("/test-api/{username}")
def admin_test_api (username: str):
    return { "message": f"Hello, {username}" }
