def aggregate_transactions(transactions):
    summary = {
        "total_amount": 0.0,
        "by_user": {},
        "failed_count": 0
    }
    for tx in transactions:
        user = tx["user_id"]
        amt = tx["amount"]
        status = tx["status"]
        if status == "success":
            summary["total_amount"] += amt
            summary["by_user"][user] = summary["by_user"].get(user, 0.0) + amt
        elif status == "failed":
            summary["failed_count"] += 1
    return summary

transactions = [
    {"user_id": "u1", "amount": 100.0, "status": "success"},
    {"user_id": "u2", "amount": 50.0, "status": "failed"},
    {"user_id": "u1", "amount": 200.0, "status": "success"}
]
print(aggregate_transactions(transactions))
