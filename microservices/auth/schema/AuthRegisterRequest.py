from pydantic import BaseModel


class AuthRegisterRequest(BaseModel):
    full_name: str
    email: str
    password: str