from fastapi import APIRouter, Request, Depends
from core.exceptions import *
from core.utils import *
from microservices.primary.dependencies import *
from microservices.primary.schema.ArticleRequest import ArticleRequest
from config import settings

# namespace ~> microservices::primary::routers::v1::article

article_router = APIRouter() # include _router at the end of the name.


#
# Add comments here
#
@article_router.post("/new", dependencies=[])
async def login (req: Request, articleBody: ArticleRequest):
    return {
        "message": "Article api require implemetation",
        "data": articleBody
    }

