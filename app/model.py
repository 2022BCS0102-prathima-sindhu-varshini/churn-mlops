import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

def predict_ml(features):
    """
    Takes engineered features and returns churn risk
    """

    # Ensure correct feature order (same as training)
    X = [[
        features["tickets_30"],
        features["monthly_charges"],
        features["complaints"]
    ]]

    # Prediction
    pred = model.predict(X)[0]

    # Convert to business label
    return "HIGH" if pred == 1 else "LOW"
