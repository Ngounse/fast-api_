from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

## // username:password
engine = create_engine("postgresql://mario:admin@localhost:5432/item_db", echo=True)

Base = declarative_base()

# to bind pur engine
SessionLocal = sessionmaker(bind=engine)