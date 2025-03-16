from pydantic import BaseModel
from pydantic.types import conint


class ProductCreate(BaseModel):
    name: str = "Iphone 12"
    price: int
    owner_id: int = 1
    
    
class ProductOut(BaseModel):
    id: int
    name: str
    price: str
    
    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):
    name: str = "admin"
    password: str
    
class UserOut(BaseModel):
    id: int
    name: str
    
    class Config:
        orm_mode = True
        
class VoteCreate(BaseModel):
    product_id: int
    dir: conint(le=1)
    

    
    
    
    