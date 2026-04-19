import pandas as pd
import random
import pickle
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, roc_auc_score, precision_score, precision_recall_curve


# ---------------------------
# STEP 1: GENERATE DATA
# ---------------------------

data = []

for _ in range(500):
    t30 = random.randint(0, 10)
    charges = random.randint(20, 100)
    complaints = random.randint(0, t30)

    # Base churn logic
    churn = 1 if (t30 > 5 or complaints > 3) else 0

    # Add noise (to avoid perfect learning)
    noise = np.random.binomial(1, 0.1)  # 10% noise
    churn = churn ^ noise  # flip label sometimes

    data.append([t30, charges, complaints, churn])


df = pd.DataFrame(data, columns=[
    "tickets_30", "monthly_charges", "complaints", "churn"
])


# ---------------------------
# STEP 2: SPLIT DATA
# ---------------------------

X = df[["tickets_30", "monthly_charges", "complaints"]]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ---------------------------
# STEP 3: TRAIN MODEL
# ---------------------------

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


# ---------------------------
# STEP 4: EVALUATION
# ---------------------------

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("F1 Score:", f1_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

# Precision-Recall
precision_vals, recall_vals, _ = precision_recall_curve(y_test, y_prob)
print("Precision-Recall computed")


# ---------------------------
# STEP 5: SAVE MODEL
# ---------------------------

pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully!")
