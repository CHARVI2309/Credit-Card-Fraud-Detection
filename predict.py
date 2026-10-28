import pandas as pd
import joblib

model = joblib.load("model/best_model.pkl")

sample = pd.DataFrame([{
    "amount":2500,
    "transaction_hour":14,
    "merchant_category":"Food",
    "foreign_transaction":0,
    "location_mismatch":0,
    "device_trust_score":92,
    "velocity_last_24h":3,
    "cardholder_age":32
}])

prediction = model.predict(sample)
probability = model.predict_proba(sample)

print(prediction)
print(probability)