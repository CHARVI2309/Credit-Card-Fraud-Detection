from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Credit Card Fraud Detection API is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No transaction data provided"
        }), 400

    required_fields = [
        "amount",
        "transaction_hour",
        "merchant_category",
        "foreign_transaction",
        "location_mismatch",
        "device_trust_score",
        "velocity_last_24h",
        "cardholder_age"
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

    return jsonify({
        "message": "Prediction endpoint is ready",
        "received_data": data
    })


if __name__ == "__main__":
    app.run(debug=True)