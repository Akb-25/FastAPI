from sqlalchemy import Boolean, String, Column, Integer
from database import Base

class Todo(Base):
    __tablename__="todos"
    id=Column(Integer,primary_key=True,index=False)
    title=Column(String)
    complete=Column(Boolean,default=False)