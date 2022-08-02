from typing import Optional
from typing import Union

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    is_offer: Union[bool, None] = None
    brand: Optional[str] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

inventory = {}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/demos/{q}")
def read_item(item_id: Optional[int] = 10001, q: Optional[str] = None):
    return {"item_id": item_id, "item_name": q}

@app.get("/get-item/{item_id}")
def read_item(item_id: int = Path(None, description="The item id", get=True)):
    return inventory[item_id]

@app.get("/get-by-name")
def read_item(*, name: str, test:int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"} 

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item already exists"}
    
    inventory[len(inventory) + 1] = item
    
    # return {"item_name": item.name, "item_id": len(inventory)}
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item does not exist"}
    if item.name != None:
        inventory[item_id].name = item.name 
    if item.price != None:
        inventory[item_id].price = item.price
    if item.is_offer != None:
        inventory[item_id].is_offer = item.is_offer
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]