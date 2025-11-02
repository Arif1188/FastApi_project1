from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.score import ScoreCreate, ScoreRead
from app.crud.score import create_score, get_scores_by_quiz
from app.db.session import get_db
from app.api.deps import get_current_student

router = APIRouter(prefix="/scores", tags=["scores"])

@router.post("/", response_model=ScoreRead)
def add_score(score: ScoreCreate, db: Session = Depends(get_db), student=Depends(get_current_student)):
    # Only allow students to add their own score
    if score.user_id != student.id:
        raise HTTPException(status_code=403, detail="Not allowed to add score for another user")
    return create_score(db, score)

@router.get("/quiz/{quiz_id}", response_model=list[ScoreRead])
def get_scores_for_quiz(quiz_id: int, db: Session = Depends(get_db)):
    return get_scores_by_quiz(db, quiz_id)