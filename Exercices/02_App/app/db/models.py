from sqlalchemy import Boolean, Column, Integer, String
#from sqlalchemy.orm import relationship

from .database import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    active = Column(Boolean)