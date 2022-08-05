from database import Base, engine
from models import Item 

print("Crating database ... ")

Base.metadata.create_all(engine)