from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.quiz import QuizRead
from app.crud.quiz import get_quizzes_by_subject, get_quiz
from app.db.session import get_db

router = APIRouter(prefix="/quizzes", tags=["quizzes"])

@router.get("/{quiz_id}", response_model=QuizRead)
def read_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz = get_quiz(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@router.get("/subject/{subject_id}", response_model=list[QuizRead])
def quizzes_by_subject(subject_id: int, db: Session = Depends(get_db)):
    return get_quizzes_by_subject(db, subject_id=subject_id)