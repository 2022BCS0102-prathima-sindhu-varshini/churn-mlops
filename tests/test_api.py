from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_high_risk():
    response = client.post("/predict-risk", json={
        "customer_id": "1",
        "monthly_charges": 80,
        "contract_type": "Month-to-Month",
        "tickets": [{"type": "complaint", "date": "2026-03-20"} for _ in range(6)]
    })
    assert response.json()["risk"] == "HIGH"

def test_low_risk():
    response = client.post("/predict-risk", json={
        "customer_id": "2",
        "monthly_charges": 20,
        "contract_type": "One Year",
        "tickets": []
    })
    assert response.json()["risk"] == "LOW"