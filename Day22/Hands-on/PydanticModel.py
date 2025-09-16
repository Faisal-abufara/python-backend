from fastapi import FastAPI
from pydantic import BaseModel, Field, validator
from typing import Literal

app = FastAPI()

class Product(BaseModel):
    name: str = Field(..., min_length=1, example="iPhone 15")
    price: float = Field(..., example=999.99)
    category: Literal["electronics", "clothing", "books"] = Field(..., example="electronics")

    @validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Price must be greater than 0')
        return value

products_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product API!"}

@app.post("/products/")
def create_product(product: Product):
    products_db.append(product)
    return {"message": "Product created successfully", "product": product}
