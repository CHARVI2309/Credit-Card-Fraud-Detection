
import os
import joblib
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "model", "best_model.pkl")
)

model = joblib.load(MODEL_PATH)

FEATURES = [
    "amount",
    "transaction_hour",
    "foreign_transaction",
    "location_mismatch",
    "device_trust_score",
    "velocity_last_24h",
    "cardholder_age",
    "merchant_category_Electronics",
    "merchant_category_Food",
    "merchant_category_Grocery",
    "merchant_category_Travel"
]

CATEGORIES = ["Electronics", "Food", "Grocery", "Travel"]


@app.route("/")
def home():
    return jsonify({
        "message": "Credit Card Fraud Detection API is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Send transaction data as JSON"
        }), 400

    required_fields = [
        "amount",
        "transaction_hour",
        "foreign_transaction",
        "location_mismatch",
        "device_trust_score",
        "velocity_last_24h",
        "cardholder_age",
        "merchant_category"
    ]

    missing_fields = [
        field for field in required_fields
        if field not in data
    ]

    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missing_fields": missing_fields
        }), 400

    if data["merchant_category"] not in CATEGORIES:
        return jsonify({
            "error": "Invalid merchant_category",
            "allowed_values": CATEGORIES
        }), 400

    try:
        row = {
            "amount": float(data["amount"]),
            "transaction_hour": float(data["transaction_hour"]),
            "foreign_transaction": float(data["foreign_transaction"]),
            "location_mismatch": float(data["location_mismatch"]),
            "device_trust_score": float(data["device_trust_score"]),
            "velocity_last_24h": float(data["velocity_last_24h"]),
            "cardholder_age": float(data["cardholder_age"])
        }

        for category in CATEGORIES:
            row[f"merchant_category_{category}"] = int(
                data["merchant_category"] == category
            )

        input_data = pd.DataFrame([row], columns=FEATURES)

        prediction = int(model.predict(input_data)[0])

        result = {
            "is_fraud": prediction,
            "status": "Fraudulent" if prediction == 1 else "Legitimate"
        }

        if hasattr(model, "predict_proba"):
            result["fraud_probability"] = round(
                float(model.predict_proba(input_data)[0][1]), 4
            )

        return jsonify(result)

    except (TypeError, ValueError):
        return jsonify({
            "error": "Feature values must be valid numbers"
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
