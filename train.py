import pandas as pd
import random

df = pd.read_csv("data/telco.csv")

def simulate_tickets():
    tickets = []
    n = random.randint(0, 7)

    for _ in range(n):
        tickets.append({
            "type": random.choice(["complaint", "query"]),
            "date": "2026-03-20"
        })
    
    return tickets

sample = df.sample(1).iloc[0]

customer_input = {
    "customer_id": sample["customerID"],
    "monthly_charges": float(sample["MonthlyCharges"]),
    "contract_type": sample["Contract"],
    "tickets": simulate_tickets()
}

print(customer_input)