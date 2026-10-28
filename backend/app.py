
import os
import math
import json
import joblib
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS
from cryptography.fernet import InvalidToken
from dotenv import load_dotenv
load_dotenv()
from security_utils import decrypt_data

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


def predict_transaction(data):
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

    if (
        not isinstance(data["merchant_category"], str)
        or data["merchant_category"] not in CATEGORIES
    ):
        return jsonify({
            "error": "Invalid merchant_category",
            "allowed_values": CATEGORIES
        }), 400

    numeric_fields = [
        "amount",
        "transaction_hour",
        "foreign_transaction",
        "location_mismatch",
        "device_trust_score",
        "velocity_last_24h",
        "cardholder_age"
    ]

    values = {}

    for field in numeric_fields:
        value = data[field]

        if isinstance(value, bool) or value is None:
            return jsonify({
                "error": f"{field} must be a valid number"
            }), 400

        try:
            value = float(value)
        except (TypeError, ValueError):
            return jsonify({
                "error": f"{field} must be a valid number"
            }), 400

        if not math.isfinite(value):
            return jsonify({
                "error": f"{field} must be finite"
            }), 400

        values[field] = value

    if values["amount"] < 0:
        return jsonify({
            "error": "Amount cannot be negative"
        }), 400

    hour = values["transaction_hour"]
    if not hour.is_integer() or not 0 <= hour <= 23:
        return jsonify({
            "error": "Transaction hour must be an integer from 0 to 23"
        }), 400

    for field in ["foreign_transaction", "location_mismatch"]:
        if values[field] not in (0, 1):
            return jsonify({
                "error": f"{field} must be 0 or 1"
            }), 400

    score = values["device_trust_score"]
    if not 0 <= score <= 1:
        return jsonify({
            "error": "Device trust score must be between 0 and 1"
        }), 400

    velocity = values["velocity_last_24h"]
    if velocity < 0 or not velocity.is_integer():
        return jsonify({
            "error": "Velocity must be a non-negative integer"
        }), 400

    age = values["cardholder_age"]
    if not age.is_integer() or not 0 <= age <= 120:
        return jsonify({
            "error": "Cardholder age must be an integer from 0 to 120"
        }), 400

    row = {
        field: values[field]
        for field in numeric_fields
    }

    for category in CATEGORIES:
        row[f"merchant_category_{category}"] = int(
            data["merchant_category"] == category
        )

    input_data = pd.DataFrame([row], columns=FEATURES)

    try:
        prediction = int(model.predict(input_data)[0])

        result = {
            "is_fraud": prediction,
            "status": (
                "Fraudulent" if prediction == 1 else "Legitimate"
            )
        }

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]
            classes = list(model.classes_)

            if 1 in classes:
                result["fraud_probability"] = round(
                    float(probabilities[classes.index(1)]), 4
                )

        return jsonify(result), 200

    except Exception:
        app.logger.exception("Fraud prediction failed")
        return jsonify({
            "error": "Prediction failed"
        }), 500


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    return predict_transaction(data)


@app.route("/predict-encrypted", methods=["POST"])
def predict_encrypted():
    data = request.get_json(silent=True)

    if (
        not isinstance(data, dict)
        or not isinstance(data.get("encrypted_data"), str)
    ):
        return jsonify({
            "error": "Send encrypted_data as a string in JSON"
        }), 400

    try:
        encrypted_bytes = data["encrypted_data"].encode("utf-8")
        decrypted_bytes = decrypt_data(encrypted_bytes)
        transaction_data = json.loads(
            decrypted_bytes.decode("utf-8")
        )

        if not isinstance(transaction_data, dict):
            return jsonify({
                "error": "Decrypted data must be a JSON object"
            }), 400

    except RuntimeError:
        app.logger.exception("Encryption key is not configured")
        return jsonify({
            "error": "Encryption is not configured on the server"
        }), 500

    except (InvalidToken, ValueError, UnicodeDecodeError,
            json.JSONDecodeError):
        app.logger.exception("Encrypted API decryption/parsing failed")
        return jsonify({
            "error": "Invalid encrypted data or JSON"
        }), 400

    except Exception:
        app.logger.exception("Unexpected encrypted API error")
        return jsonify({
            "error": "Encrypted request processing failed"
        }), 500

    return predict_transaction(transaction_data)


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")

from dotenv import load_dotenv
load_dotenv()
