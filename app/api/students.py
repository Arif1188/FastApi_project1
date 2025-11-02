from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_current_student
from app.crud.score import get_scores_by_user
from app.schemas.score import ScoreRead
from app.db.session import get_db

router = APIRouter(prefix="/students", tags=["students"])

@router.get("/scores", response_model=list[ScoreRead])
def get_my_scores(db: Session = Depends(get_db), student=Depends(get_current_student)):
    return get_scores_by_user(db, user_id=student.id)