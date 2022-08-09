from sqlalchemy import (Boolean, Column, Float, ForeignKey, Integer, String,
                        Text)

from database import Base


class UserAuth(Base):
    __tablename__ = "userAuth"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    permission = Column(String(15))
    active = Column(Boolean, default=True)

    def __repr__(self):
        # return f"<Item name={self.name} price={self.price}>"
        return f"<Item(username='{self.username}', hashed_password='{self.hashed_password}',email='{self.email}', permission='{self.permission}', active='{self.active}')>"

# from models import Item
# new_item=Item(name="milk", price=2000, description="milk", on_offer=True)
