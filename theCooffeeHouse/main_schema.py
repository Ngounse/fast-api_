from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseModel

import models
from database import SessionLocal

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class UserAuth(BaseModel): #serlializer 
    id:int
    username:str
    password: str
    permission:str
    active: bool

    class Config:
        orm_mode = True #to use sqlalchemy

class UserLogin(BaseModel): #serlializer 
    username:str
    password: str

    class Config:
        orm_mode = True #to use sqlalchemy

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
db = SessionLocal()

def get_password_hash(password):
    return pwd_context.hash(password)

@app.get("/user", response_model=List[UserAuth], status_code=200)
def get_all_user():
    items = db.query(models.UserAuth).all()

    return items

@app.post("/login-user/",response_model=UserLogin, status_code=status.HTTP_200_OK)
def login_user( item :UserLogin):
    print('item=======', item)
    db_user = db.query(models.UserAuth).filter(models.UserAuth.username == item.username).first()
    db_passwd = db.query(models.UserAuth).filter(models.UserAuth.password == item.password).first()
    
    print(db_user, 'db_user ::: ')
    print(db_passwd, 'db_passwd ::: ')
    if db_user is None:
        raise HTTPException(status_code=400,detail="User does not exists")

    if db_passwd is None:
        raise HTTPException(status_code=400,detail="Incorrect password")

    # items = db.query(models.UserAuth).all()
    secret_key = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    
    raise HTTPException(status_code=200,detail=secret_key)

@app.post("/create-user", response_model=UserAuth, status_code=status.HTTP_201_CREATED)
def create_an_user(user: UserAuth):
    db_item = db.query(models.UserAuth).filter(models.UserAuth.username == user.username).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="User already exists")

    new_user = models.UserAuth(
        username= user.username,
        password= user.password,
        permission= user.permission,
        active= user.active
    )
    

    db.add(new_user)
    db.commit()

    return new_user

# @app.put('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
# def update_an_item(item_id:int,item:Item):
#     item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
#     item_to_update.name=item.name
#     item_to_update.price=item.price
#     item_to_update.description=item.description
#     item_to_update.on_offer=item.on_offer

#     db.commit()

#     return item_to_update

# @app.delete("/item/{item_id}")
# def delete_an_item(item_id:int):
#     item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()
    
#     if item_to_delete is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
#     db.delete(item_to_delete)
#     db.commit()
    
#     return item_to_delete
