from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_current_teacher
from app.schemas.quiz import QuizCreate, QuizRead
from app.crud.quiz import create_quiz, get_quizzes_by_creator
from app.db.session import get_db

router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.post("/quizzes", response_model=QuizRead)
def create_quiz_teacher(quiz: QuizCreate, db: Session = Depends(get_db), teacher=Depends(get_current_teacher)):
    return create_quiz(db, quiz, creator_id=teacher.id)

@router.get("/quizzes", response_model=list[QuizRead])
def get_my_quizzes(db: Session = Depends(get_db), teacher=Depends(get_current_teacher)):
    return get_quizzes_by_creator(db, creator_id=teacher.id)