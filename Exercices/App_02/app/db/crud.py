from typing import List
from . import models, schemas
from sqlalchemy.orm import Session


def get_case(db: Session, case_id: int):

    return db.query(models.Case).filter(models.Case.id == case_id).first()


def get_cases(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Case).offset(skip).limit(limit).all()


def create_case(db: Session, case: schemas.CaseCreate):
    db_case = models.Case(name=case.name)
    db.add(CaseBase)
    db.commit()
    db.refresh(CaseBase)

    return CaseBase


def create_covid_by_country(db: Session, covid_data: List[schemas.CovidByCountrySchema]):
    for data in covid_data:
        db_data = models.CovidByCountryModel(**data.dict())
        db.add(db_data)
    db.commit()


def create_covid_worldwide(db: Session, covid_data: List[schemas.CovidWorldwideSchema]):
    for data in covid_data:
        db_data = models.CovidWorldwideModel(**data.dict())
        db.add(db_data)
    db.commit()