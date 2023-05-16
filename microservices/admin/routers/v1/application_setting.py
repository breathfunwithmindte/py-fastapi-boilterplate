from fastapi import APIRouter, Request, Depends
from core.exceptions import *
from core.utils import *
from microservices.admin.dependencies import passport, admin_only
from config import settings


# namespace ~> microservices::admin::routers::v1::application_setting

application_setting_router = APIRouter() # include _router at the end of the name.

#
# Add comments here
#
@application_setting_router.get("/test", dependencies=[Depends(passport), Depends(admin_only)])
async def test (req: Request):
    return {
        "test": "Hello World",
        "message": "API working correctly",
        "user": req.state.user
    }

