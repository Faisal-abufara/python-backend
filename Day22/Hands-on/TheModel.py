from pydantic import BaseModel, Field
from typing import Literal

class Product(BaseModel):
    name: str = Field(..., min_length=1, example="iPhone 15")
    price: float = Field(..., gt=0, example=999.99)
    category: Literal["electronics", "clothing", "books"] = Field(..., example="electronics")
