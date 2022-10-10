from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

## // username:password
engine = create_engine("postgresql://mario:admin@db:5432/item_db")
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
# to bind pur engine
# SessionLocal = sessionmaker(bind=engine)
