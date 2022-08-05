from database import Base
from sqlalchemy import String, Column, Integer, ForeignKey, Boolean, Float, Text

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    price = Column(Float, nullable=False)
    description = Column(Text)
    on_offer = Column(Boolean, default=False)

    def __repr__(self):
        # return f"<Item name={self.name} price={self.price}>"
        return f"<Item(name='{self.name}', description='{self.description}', price='{self.price}', on_offer='{self.on_offer}')>"

# from models import Item
# new_item=Item(name="milk", price=2000, description="milk", on_offer=True)