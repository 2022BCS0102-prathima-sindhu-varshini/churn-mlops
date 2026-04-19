import pickle

model = pickle.load(open("model.pkl", "rb"))

def predict_ml(features):
    try:
        X = [[
            features["tickets_30"],
            features["monthly_charges"],
            features["complaints"]
        ]]
        
        pred = model.predict(X)[0]
        return "HIGH" if pred == 1 else "LOW"

    except Exception as e:
        print("ERROR:", e)
        return "ERROR"
