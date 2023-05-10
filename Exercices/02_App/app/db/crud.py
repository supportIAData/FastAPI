from sqlalchemy.orm import Session
from . import models, schemas

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