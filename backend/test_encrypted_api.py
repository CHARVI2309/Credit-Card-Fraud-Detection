
import json
import requests
from security_utils import encrypt_data

URL = "http://127.0.0.1:5000/predict-encrypted"

transaction = {
    "amount": 5000,
    "transaction_hour": 14,
    "foreign_transaction": 0,
    "location_mismatch": 0,
    "device_trust_score": 0.9,
    "velocity_last_24h": 2,
    "cardholder_age": 25,
    "merchant_category": "Electronics"
}

encrypted = encrypt_data(
    json.dumps(transaction).encode("utf-8")
).decode("utf-8")

response = requests.post(
    URL,
    json={"encrypted_data": encrypted},
    timeout=10
)

print("Valid transaction status:", response.status_code)
print("Response:", response.text)

bad_response = requests.post(
    URL,
    json={"encrypted_data": "invalid_data"},
    timeout=10
)

print("Invalid transaction status:", bad_response.status_code)
print("Response:", bad_response.text)
