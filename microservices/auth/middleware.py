from fastapi import HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware
from core.exceptions import *

class PrimaryMicroserviceMiddleware(BaseHTTPMiddleware):
    def __init__(
            self,
            app
    ):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        # do something with the request object, for example
        print ("[MICROSERVICE::AUTH::MIDDLEWARE] ::~>", request.url)
        
        # process the request and get the response    
        response = await call_next(request)
        return response