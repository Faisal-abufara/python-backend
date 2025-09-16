from pydantic import BaseModel, Field, model_validator
from typing import Literal

class Product(BaseModel):
    name: str = Field(..., min_length=1, example="iPhone 15")
    price: float = Field(..., example=999.99)
    category: Literal["electronics", "clothing", "books"] = Field(..., example="electronics")

    @model_validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Price must be greater than 0')
        return value
