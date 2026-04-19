from datetime import datetime

def extract_features(customer):
    tickets = customer["tickets"]
    now = datetime.now()

    t7, t30, t90 = 0, 0, 0
    complaints = 0
    queries = 0
    dates = []

    for t in tickets:
        d = datetime.strptime(t["date"], "%Y-%m-%d")
        days = (now - d).days
        dates.append(d)

        if days <= 7: t7 += 1
        if days <= 30: t30 += 1
        if days <= 90: t90 += 1

        if t["type"] == "complaint":
            complaints += 1
        else:
            queries += 1

    # time gap
    if len(dates) > 1:
        dates.sort()
        time_gap = (dates[-1] - dates[0]).days / len(dates)
    else:
        time_gap = 0

    return {
        "tickets_7": t7,
        "tickets_30": t30,
        "tickets_90": t90,
        "complaints": complaints,
        "queries": queries,
        "monthly_charges": customer["monthly_charges"],
        "time_gap": time_gap
    }
