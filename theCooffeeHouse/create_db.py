from database import Base, engine
from models import UserAuth

print("Crating database ... ")

Base.metadata.create_all(engine)

## run this script to create the database
