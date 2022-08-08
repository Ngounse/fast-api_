from typing import List, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

import models
from database import SessionLocal

app = FastAPI()

class UserAuth(BaseModel): #serlializer 
    id:int
    username:str
    password: str
    permission:str
    active: bool

    class Config:
        orm_mode = True #to use sqlalchemy

class UserLogin(BaseModel): #serlializer 
    id:Optional[int]
    username:str
    password: str
    permission:Optional[str] = None
    active: Optional[bool] = None

    class Config:
        orm_mode = True #to use sqlalchemy

db = SessionLocal()

@app.get("/user", response_model=List[UserAuth], status_code=200)
def get_all_items():
    items = db.query(models.UserAuth).all()
    
    return items

# @app.get("/item/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
# def get_an_item(item_id:int):
#     item = db.query(models.Item).filter(models.Item.id == item_id).first()esponse_model=List[UserAuth], status_code=200)
def get_all_user():
    items = db.query(models.UserAuth).all()

    return items
#     return item

@app.post("/login-user/{username}{password}", response_model=UserLogin, status_code=status.HTTP_200_OK)
def get_a_user(username: Optional[str],password: Optional[str], user: UserAuth):
    db_user = db.query(models.UserAuth).filter(models.UserAuth.username == username).first()
    db_passwd = db.query(models.UserAuth).filter(models.UserAuth.password == password).first()
    
    print(db_user, 'db_user ::: ')
    print(db_user, 'db_passwd ::: ')
    if db_user is None:
        raise HTTPException(status_code=400,detail="User does not exists")

    if db_passwd is None:
        raise HTTPException(status_code=400,detail="Incorrect password")

    items = db.query(models.UserAuth).all()
    return items

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
