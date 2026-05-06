from pydantic import BaseModel
from typing import List

class SaleItem(BaseModel):
    dish: str
    cost_price: float
    selling_price: float
    quantity: int


class SalesRequest(BaseModel):
    sales: List[SaleItem]
