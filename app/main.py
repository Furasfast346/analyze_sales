from fastapi import FastAPI, HTTPException
from .schemas import SalesRequest
from .utils import analyze_sales_data

app = FastAPI()


@app.post('/analyze_sales')
async def analyze_sales(data: SalesRequest):
    # Если Пришёл пустой запрос - вызываем ошибку Bad Request
    if not data.sales:
        raise HTTPException(status_code=400, detail="No sales data provided")

    return analyze_sales_data(data.sales)
