import pandas as pd
import random
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, roc_auc_score, precision_score

data = []

for _ in range(300):
    t30 = random.randint(0, 10)
    charges = random.randint(20, 100)
    complaints = random.randint(0, t30)

    churn = 1 if t30 > 5 or complaints > 3 else 0

    data.append([t30, charges, complaints, churn])

df = pd.DataFrame(data, columns=["t30", "charges", "complaints", "churn"])

X = df[["t30", "charges", "complaints"]]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("F1:", f1_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_pred))

pickle.dump(model, open("model.pkl", "wb"))

print("Model saved!")
