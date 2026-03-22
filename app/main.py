from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.model import predict_ml
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

class Ticket(BaseModel):
    type: str
    date: str

class Customer(BaseModel):
    customer_id: str
    monthly_charges: float
    contract_type: str
    tickets: List[Ticket]

@app.post("/predict-risk")
def predict_risk(customer: Customer):
    logging.info(f"Request for {customer.customer_id}")
    tickets_30 = len(customer.tickets)
    risk = predict_ml(tickets_30, customer.monthly_charges)
    return {"risk": risk}