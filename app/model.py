import pickle

model = pickle.load(open("model.pkl", "rb"))

def predict_ml(tickets_30, charges):
    pred = model.predict([[tickets_30, charges]])
    return "HIGH" if pred[0] == 1 else "LOW"