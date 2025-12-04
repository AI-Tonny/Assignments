from pydantic import BaseModel, Field
from typing import List

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float
    quantity: int

class ProductChange(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float
    quantity: int

class ProductResponse(BaseModel):
    name: str
    price: float
    quantity: int

class ProductOneResponse(BaseModel):
    status: int
    success: bool
    data: ProductResponse

class ProductsResponse(BaseModel):
    status: int
    success: bool
    data: List[ProductResponse]

class ProductCreatedResponse(BaseModel):
    status: int
    success: bool
    data: ProductResponse

class ProductChangedResponse(BaseModel):
    status: int
    success: bool
    data: ProductResponse

class ProductDeletedResponse(BaseModel):
    status: int
    success: bool