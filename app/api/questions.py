from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.question import QuestionCreate, QuestionRead
from app.crud.question import create_question, get_questions_by_quiz
from app.db.session import get_db
from app.api.deps import get_current_teacher

router = APIRouter(prefix="/questions", tags=["questions"])

@router.post("/", response_model=QuestionRead)
def create_new_question(question: QuestionCreate, db: Session = Depends(get_db), teacher=Depends(get_current_teacher)):
    return create_question(db, question)

@router.get("/quiz/{quiz_id}", response_model=list[QuestionRead])
def list_questions_for_quiz(quiz_id: int, db: Session = Depends(get_db)):
    return get_questions_by_quiz(db, quiz_id)