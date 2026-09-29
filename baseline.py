import pandas as pd

df = pd.read_csv("customer-churn-training.csv")

df["baseline_prediction"] = (
    (df["last_login_days"] > 10) |
    (df["support_tickets"] >= 3)
).astype(int)

print(df[[
    "customer_id",
    "churned",
    "baseline_prediction"
]])

accuracy = (
    df["churned"] == df["baseline_prediction"]
).mean()

print("\nBaseline Accuracy:", accuracy)