from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String

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
        return f"<Item(username='{self.username}', hashed_password='{self.hashed_password}',email='{self.email}', permission='{self.permission}', active='{self.active}')>"

# from models import Item
# new_item=Item(name="milk", price=2000, description="milk", on_offer=True)

class ProductItem(Base):
    __tablename__ = "productItem"
    id = Column(Integer, primary_key=True, index=True)
    pro_name = Column(String(50), nullable=False)
    pro_price = Column(Float(20), nullable=False)
    pro_type = Column(String(20), nullable=False)
    date_create = Column(String(60), nullable=False)
    last_update = Column(String(60), nullable=False)
    username = Column(String(50), nullable=False)
    is_offer = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Item(product_name='{self.pro_name}', product_price='{self.pro_price}', product_type='{self.pro_type}',date_create='{self.date_create}',last_update='{self.last_update}', username='{self.username}', is_offer='{self.is_offer}')>"
