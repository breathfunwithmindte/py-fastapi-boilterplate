from fastapi import FastAPI, status, Depends, HTTPException, Request, APIRouter
from fastapi.responses import JSONResponse
from config import settings
from http import HTTPStatus
from core.exceptions import register_exceptions, NonAuthenticatedException, ForbiddenException
from microservices.admin.admin import admin_microservice
from microservices.auth.auth import auth_microservice
from microservices.primary.primary import primary_microservice


def create_app() -> FastAPI: 
    
    _app = FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        docs_url="/docs",
    )


    register_exceptions(_app)


    register_exceptions(admin_microservice)
    register_exceptions(auth_microservice)
    register_exceptions(primary_microservice)


    _app.mount(settings.ADMIN_API_V1_PREFIX, admin_microservice)
    _app.mount(settings.AUTH_API_V1_PREFIX, auth_microservice)
    _app.mount(settings.PRIMARY_API_V1_PREFIX, primary_microservice)


    # _app.mount(settings.PRIMARY_API_V1_PREFIX, primary_app)
    

    return _app
    

    