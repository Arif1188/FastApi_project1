from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.subject import SubjectCreate, SubjectRead
from app.crud.subject import create_subject, get_subjects
from app.db.session import get_db
from app.api.deps import get_current_teacher

router = APIRouter(prefix="/subjects", tags=["subjects"])

@router.post("/", response_model=SubjectRead)
def create_new_subject(subject: SubjectCreate, db: Session = Depends(get_db), teacher=Depends(get_current_teacher)):
    return create_subject(db, subject)

@router.get("/", response_model=list[SubjectRead])
def list_subjects(db: Session = Depends(get_db)):
    return get_subjects(db)