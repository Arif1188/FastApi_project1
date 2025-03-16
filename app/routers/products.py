from fastapi import APIRouter, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import Products,User,Vote
from app.schemas import ProductCreate
from app.oauth2 import get_current_user
from sqlalchemy import func, select

router = APIRouter(tags=["Products"])


@router.get("/")
async def get_products(db: Session = Depends(get_db)):
    querry = select(Products.owner_id, User.name.label("user_name"), Products.name, Products.price).join(
        User, Products.owner_id == User.id
    )
    results = db.execute(querry).all()
    response = [
        {
            "owner_id": row[0],
            "user_name": row[1],
            "product_name": row[2],
            "price": row[3]
        }
        for row in results
    ]
    print(querry)
    print(results)
    print(response)
    return response

@router.post("/create_product")
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    products = Products(name = product.name, price = product.price, owner_id = product.owner_id)
    db.add(products)
    db.commit()
    db.refresh(products)
    return products

@router.put("/update_product/{id}")
async def update_product(id:int, product: ProductCreate, db: Session = Depends(get_db)):
    products = db.query(Products).filter(Products.id==id).first()
    products.name = product.name
    products.price = product.price
    db.commit()
    db.refresh(products)
    return products

@router.delete("/delete_product/{id}")
async def delete_product(id:int, db:Session = Depends(get_db)):
    product = db.query(Products).filter(Products.id == id).first()
    db.delete(product)
    db.commit()
    return "Deleted Successfully"

