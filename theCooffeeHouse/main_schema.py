from datetime import datetime, time, timedelta
from typing import List, Optional

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from .database import SessionLocal
from .models import ProductItem as modelsProductItem
from .models import UserAuth as modelsUserAuth

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:8000",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserAuth(BaseModel): #serlializer 
    id:int
    username:str
    hashed_password: str
    email: str | None = '@gmail.com'
    permission:str | None = 'user'
    active: bool

    class Config:
        orm_mode = True #to use sqlalchemy

class UserLogin(BaseModel): #serlializer 
    email:str
    hashed_password: str

    class Config:
        orm_mode = True #to use sqlalchemy

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
db = SessionLocal()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)
class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db
        return UserInDB(**user_dict)
class Token(BaseModel):
    access_token: str
    token_type: str

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token' : form_data.username + 'token'}

@app.get('/')
async def index(token: str = Depends(oauth2_scheme)):
    return {'the_token' : token}


@app.get("/user", response_model=List[UserAuth], status_code=200)
async def get_all_user(token: str = Depends(oauth2_scheme)):
    items = db.query(modelsUserAuth).all()

    return items

@app.post("/user-login/", status_code=status.HTTP_200_OK)
async def login_user( item :UserLogin):
    print('item=======', item)
    db_item = db.query(modelsUserAuth).filter(modelsUserAuth.email == item.email).first()

    info_user = modelsUserAuth(
        email= item.email,
        hashed_password= item.hashed_password,
    )
    print(info_user, 'info_user ::: ')
    if db_item is None:
        raise HTTPException(status_code=400,detail="Email does not exists.")

    if not verify_password(item.hashed_password, db_item.hashed_password):
        raise HTTPException(status_code=400,detail="Incorrect password.")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    print('access_token_expires =====', access_token_expires)
    access_token = create_access_token(
        data={"name": db_item.username, "permission": db_item.permission,"active": db_item.active, }, expires_delta=access_token_expires
    )
    print('access_token ====', access_token)
    
    # raise HTTPException(status_code=200,detail=access_token)
    return JSONResponse(content={"access_token": access_token, "token_type": "bea326rer"}) 


@app.post("/user-create", response_model=UserAuth, status_code=status.HTTP_201_CREATED)
def create_a_user(user: UserAuth):
    db_item = db.query(modelsUserAuth).filter(modelsUserAuth.username == user.username).first()
    db_item = db.query(modelsUserAuth).filter(modelsUserAuth.email == user.email).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="User or Email already exists.")
    hashed_password = get_password_hash(user.hashed_password)

    new_user = modelsUserAuth(
        username= user.username,
        hashed_password= hashed_password,
        email= user.email,
        permission= user.permission,
        active= user.active
    )

    db.add(new_user)
    db.commit()

    return new_user

@app.put('/user-update/{username}',response_model=UserAuth,status_code=status.HTTP_200_OK)
async def update_user(username:str,item:UserAuth, token: str = Depends(oauth2_scheme)):
    user_to_update=db.query(modelsUserAuth).filter(modelsUserAuth.username==username).first()
    if user_to_update is None:
        raise HTTPException(status_code=404,detail="User not found.")
    # user_to_update.username=item.username
    user_to_update.hashed_password=get_password_hash(item.hashed_password)
    # user_to_update.email=item.email
    # user_to_update.permission=item.permission
    user_to_update.active=item.active

    db.commit()

    return user_to_update

@app.delete("/user-delete/{username}")
async def delete_a_user(username:str, token: str = Depends(oauth2_scheme)):
    item_to_delete=db.query(modelsUserAuth).filter(modelsUserAuth.username==username).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    db.delete(item_to_delete)
    db.commit()

    return item_to_delete


##  Product item

class ProductItem(BaseModel): #serlializer 
    # id:int
    pro_name:str | None = 'Ice late'
    pro_price: float| None = 1.49
    pro_type: str | None = 'coffee'
    date_create: str | None = 'Auto now'
    last_update: str | None = 'Auto now'
    username:str | None = 'user'
    is_offer: bool | None = False

    class Config:
        orm_mode = True #to use sqlalchemy

@app.get("/item", response_model=List[ProductItem], status_code=200)
def get_all_product():
    items = db.query(modelsProductItem).all()

    return items

@app.post("/item", response_model=ProductItem, status_code=status.HTTP_201_CREATED)
async def create_product(item: ProductItem):
     

    new_item = modelsProductItem(
        pro_name= item.pro_name,
        pro_price= item.pro_price,
        pro_type= item.pro_type,
        date_create= datetime.now(),
        last_update= 'Not yet updated',
        username= item.username,
        is_offer= item.is_offer
    )

    db.add(new_item)
    db.commit()

    return new_item

@app.put('/item/{pro_id}',response_model=ProductItem,status_code=status.HTTP_200_OK)
async def update_product(pro_id:str,item:ProductItem, token: str = Depends(oauth2_scheme)):
    item_to_update=db.query(modelsProductItem).filter(modelsProductItem.id==pro_id).first()
    if item_to_update is None:
        raise HTTPException(status_code=404,detail="Product not found.")
    item_to_update.pro_name=item.pro_name
    item_to_update.pro_price=item.pro_price
    item_to_update.pro_type=item.pro_type
    # item_to_update.date_create=
    item_to_update.last_update= datetime.now(),
    item_to_update.username=item.username
    item_to_update.is_offer=item.is_offer

    db.commit()

    return item_to_update

@app.delete("/item/{pro_id}")
async def delete_product(pro_id:str, token: str = Depends(oauth2_scheme)):
    item_to_delete=db.query(modelsProductItem).filter(modelsProductItem.id==pro_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found.")

    db.delete(item_to_delete)
    db.commit()

    raise HTTPException(status_code=status.HTTP_200_OK, detail="Product deleted.")
    return 


@app.get("/demo", )
def demo():
    return { "message": "hello world"}

@app.get("/demo1", )
def demo_one():
    return { "message": "hello world"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
