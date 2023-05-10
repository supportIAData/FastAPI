from typing import Union

from pydantic import BaseModel

class CaseBase(BaseModel):
    name: str
    active: bool

class CaseCreate(CaseBase):
    pass

class Case(CaseBase):
    id: int

    # class Config:
    #     orm_mode = True