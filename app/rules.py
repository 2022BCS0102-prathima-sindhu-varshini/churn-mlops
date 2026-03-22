from datetime import datetime

def compute_risk(customer):
    tickets = customer.tickets
    now = datetime.now()

    count_30 = 0
    complaint = False

    for t in tickets:
        ticket_date = datetime.strptime(t.date, "%Y-%m-%d")
        if (now - ticket_date).days <= 30:
            count_30 += 1
        if t.type.lower() == "complaint":
            complaint = True

    if count_30 > 5:
        return "HIGH"

    if customer.monthly_charges > 70 and count_30 >= 3:
        return "MEDIUM"

    if customer.contract_type == "Month-to-Month" and complaint:
        return "HIGH"

    return "LOW"