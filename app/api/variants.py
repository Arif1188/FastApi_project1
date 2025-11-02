from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.variant import VariantCreate, VariantRead
from app.crud.variant import create_variant, get_variants_by_question
from app.db.session import get_db
from app.api.deps import get_current_teacher

router = APIRouter(prefix="/variants", tags=["variants"])

@router.post("/", response_model=VariantRead)
def create_new_variant(variant: VariantCreate, db: Session = Depends(get_db), teacher=Depends(get_current_teacher)):
    return create_variant(db, variant)

@router.get("/question/{question_id}", response_model=list[VariantRead])
def list_variants_for_question(question_id: int, db: Session = Depends(get_db)):
    return get_variants_by_question(db, question_id)