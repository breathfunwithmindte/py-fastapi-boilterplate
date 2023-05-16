from pydantic import BaseModel
from typing import Optional

class ArticleRequest(BaseModel):
    title: str
    description: Optional[str]