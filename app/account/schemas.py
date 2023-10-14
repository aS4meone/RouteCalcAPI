from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    email: str
    hashed_password: str
    current_address: str


class UserRequest(BaseModel):
    username: str
    email: str
    hashed_password: str
    current_address: str


class Token(BaseModel):
    access_token: str
    token_type: str
