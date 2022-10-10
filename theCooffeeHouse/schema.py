from typing import Optional

from pydantic import BaseModel


class UserAuth(BaseModel): #serlializer 
    id:int
    username:str
    hashed_password: str
    email: str | None = '@gmail.com'
    permission:str | None = 'user'
    active: bool

    class Config:
        orm_mode = True #to use sqlalchemy


class Configuration(BaseModel):
    modelUrl: str
    frequency: int
    federated: bool

    class Config:
        orm_mode = True
