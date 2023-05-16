from pydantic import BaseModel


class AuthLoginRequest(BaseModel):
    login_value: str
    password: str