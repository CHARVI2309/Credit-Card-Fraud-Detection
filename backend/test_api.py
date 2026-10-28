
# import requests

# transaction = {
#     "amount": 5000,
#     "transaction_hour": 14,
#     "foreign_transaction": 0,
#     "location_mismatch": 0,
#     "device_trust_score": 0.9,
#     "velocity_last_24h": 2,
#     "cardholder_age": 25,
#     "merchant_category": "Electronics"
# }

# response = requests.post(
#     "http://127.0.0.1:5000/predict",
#     json=transaction
# )

# print("Status Code:", response.status_code)
# print("Response:", response.text)


# # Test missing transaction fields
# bad_response = requests.post(
#     "http://127.0.0.1:5000/predict",
#     json={"amount": 5000}
# )

# print("Invalid Input Status:", bad_response.status_code)
# print("Invalid Input Response:", bad_response.text)

import requests

BASE_URL = "http://127.0.0.1:5000"

# Test 1: Valid transaction
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

response = requests.post(
    f"{BASE_URL}/predict",
    json=transaction
)
print("\nTEST 1 - Valid Transaction")
print("Status:", response.status_code)
print("Response:", response.text)

# Test 2: Missing fields
response = requests.post(
    f"{BASE_URL}/predict",
    json={"amount": 5000}
)
print("\nTEST 2 - Missing Fields")
print("Status:", response.status_code)
print("Response:", response.text)

# Test 3: Fraud-like transaction
fraud_like_transaction = {
    "amount": 25000,
    "transaction_hour": 3,
    "foreign_transaction": 1,
    "location_mismatch": 1,
    "device_trust_score": 0.1,
    "velocity_last_24h": 15,
    "cardholder_age": 25,
    "merchant_category": "Electronics"
}

response = requests.post(
    f"{BASE_URL}/predict",
    json=fraud_like_transaction
)
print("\nTEST 3 - Fraud-like Transaction")
print("Status:", response.status_code)
print("Response:", response.text)

print("\nAll API tests completed.")
