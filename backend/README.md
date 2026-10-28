# Credit Card Fraud Detection Backend

Flask REST API for the Credit Card Fraud Detection System.

## Features

- Fraud prediction using a trained machine learning model.
- Input validation for transaction data.
- Encrypted transaction prediction using Fernet encryption.
- Health-check endpoint.
- API testing for valid and invalid requests.

## Requirements

- Python 3
- Dependencies listed in `requirements.txt`
- Trained model at `model/best_model.pkl`
- Fernet encryption key configured as an environment variable.

## Installation

From the project root directory:

```bash
pip install -r backend/requirements.txt
```

## Run the Backend

Open PowerShell and run:

```powershell
cd backend
$env:FERNET_KEY="YOUR_PRIVATE_FERNET_KEY"
python app.py
```

Generate your own key locally and use the same key when testing encrypted requests. Do not commit the key to GitHub.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Check API health |
| POST | `/predict` | Predict fraud from transaction data |
| POST | `/predict-encrypted` | Predict fraud from encrypted transaction data |

The encrypted endpoint expects JSON containing an `encrypted_data` field.

## Run Tests

From the project root directory:

```powershell
python backend/test_encryption.py
python backend/test_api.py
python backend/test_encrypted_api.py
```

## Response

Prediction endpoints return the fraud probability, fraud classification, and transaction status.

**Note:** This Flask development server is intended for development and testing, not production deployment.
