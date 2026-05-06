import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_sales_valid():
    payload = {
        "sales": [
            {"dish": "Паста", "cost_price": 100, "selling_price": 300, "quantity": 10},
            {"dish": "Салат", "cost_price": 50, "selling_price": 150, "quantity": 5}
        ]
    }
    response = client.post("/analyze_sales", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "top_margin_dishes" in data
    assert "loss_making" in data
    assert "total_revenue" == 3000 + 750 == 3750

def test_analyze_sales_empty():
    response = client.post("/analyze_sales", json={"sales": []})
    assert response.status_code == 400
    assert "No sales data provided" in response.text

def test_analyze_sales_missing_field():
    payload = {"sales": [{"dish": "Паста", "cost_price": 100, "selling_price": 300}]}
    response = client.post("/analyze_sales", json=payload)
    assert response.status_code == 422  # Validation error