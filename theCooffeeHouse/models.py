from sqlalchemy import (Boolean, Column, Float, ForeignKey, Integer, String,
                        Text)

from database import Base


class UserAuth(Base):
    __tablename__ = "userAuth"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    permission = Column(Text)
    active = Column(Boolean, default=True)

    def __repr__(self):
        # return f"<Item name={self.name} price={self.price}>"
        return f"<Item(name='{self.username}', description='{self.password}', price='{self.permission}', on_offer='{self.active}')>"

# from models import Item
# new_item=Item(name="milk", price=2000, description="milk", on_offer=True)
