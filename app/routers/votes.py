from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2
from app.models import Products, Vote
from app.schemas import VoteCreate
from app.database import get_db
from app.oauth2 import get_current_user


router = APIRouter(
    tags=['Vote']
)

@router.post("/vote")
async def vote_product(voteCreate: VoteCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    
    # Checking if the product exists:
    product = db.query(Products).filter(Products.id == voteCreate.product_id).first()
    if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id: {voteCreate.product_id} does not exist")
            
    # Checking if the user already voted:     
    existing_vote = db.query(Vote).filter(Vote.product_id == voteCreate.product_id,
                                           Vote.user_id == current_user.id).first()
    
    if voteCreate.dir == 1:
        if existing_vote:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"user {current_user.id} has alredy voted on post {voteCreate.product_id}")
                
        new_vote = Vote(product_id = voteCreate.product_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Successfully added vote"}
    else:
        if not existing_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")
            
        vote = db.query(Vote).filter(Vote.product_id == voteCreate.product_id).first()
        db.delete(vote)
        db.commit()
        return {"message": "successfully deleted vote"}
    
