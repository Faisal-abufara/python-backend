from fastapi import FastAPI
from fastapi import Query
from typing import Optional

APP = FastAPI()

items_db = {
    1: {"name": "Apple", "category": "fruit", "price": 1.5},
    2: {"name": "Banana", "category": "fruit", "price": 0.8},
    3: {"name": "Carrot", "category": "vegetable", "price": 1.0},
    4: {"name": "Steak", "category": "meat", "price": 10.0},
}

@APP.get("/items/{item_id}")
def get_item(
    item_id: int,
    category: Optional[str] = Query(None),
    max_price: Optional[float] = Query(None)
):
    item = items_db.get(item_id)

    if not item:
        return {"error": "Item not found"}

    if category and item["category"] != category:
        return {"error": f"No item found with category '{category}'"}

    if max_price is not None and item["price"] > max_price:
        return {"error": f"Item price exceeds {max_price}"}

    return {"item_id": item_id, "data": item}
