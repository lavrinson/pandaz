from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Настройка базы данных
DATABASE_URL = 'sqlite:///users.db'
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    profile_photo = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
