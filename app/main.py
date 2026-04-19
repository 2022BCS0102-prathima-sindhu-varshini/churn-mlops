from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import logging

from ml.features import extract_features
from app.model import predict_ml

app = FastAPI()

logging.basicConfig(level=logging.INFO)


# ----------- SCHEMA -----------

class Ticket(BaseModel):
    type: str
    date: str


class Customer(BaseModel):
    customer_id: str
    monthly_charges: float
    contract_type: str
    tickets: List[Ticket]


# ----------- API -----------

@app.get("/")
def home():
    return {"message": "ML Churn Prediction API Running"}


@app.post("/predict-risk")
def predict_risk(customer: Customer):
    logging.info(f"Request for {customer.customer_id}")

    # Convert input to dictionary
    customer_dict = customer.dict()

    # Feature engineering
    features = extract_features(customer_dict)

    # Debug print (you can keep for screenshots)
    print("FEATURES:", features)

    # ML prediction
    risk = predict_ml(features)

    return {"risk": risk}
