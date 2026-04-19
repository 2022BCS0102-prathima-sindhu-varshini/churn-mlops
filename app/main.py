from ml.features import extract_features
from app.model import predict_ml

@app.post("/predict-risk")
def predict_risk(customer: Customer):
    customer_dict = customer.dict()

    features = extract_features(customer_dict)

    print("FEATURES:", features)   # debug

    risk = predict_ml(features)

    return {"risk": risk}
