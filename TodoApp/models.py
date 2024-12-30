from pydantic import BaseModel, Field
from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique = True)
    username = Column(String, unique = True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default = True)
    role = Column(String)
    phone_number = Column(String)

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
    phone_number: str

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_lenght = 6)


class Token(BaseModel):
    access_token: str
    token_type: str


class Todos(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default = False)
    owner_id = Column(Integer, ForeignKey("users.id"))


class TodoRequest(BaseModel):
    title: str = Field(min_length = 3)
    description: str = Field(min_length = 3, max_length= 100)
    priority: int = Field(gt = 0, lt = 6)
    complete: bool