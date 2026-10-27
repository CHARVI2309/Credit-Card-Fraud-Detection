# Credit-Card-Fraud-Detection
# 💳 Credit Card Fraud Detection System Using Machine Learning

## 📌 Overview

The **Credit Card Fraud Detection System** is a Machine Learning project designed to identify fraudulent credit card transactions. The project analyzes transaction data, preprocesses the dataset, trains multiple classification models, evaluates their performance, and deploys the best-performing model for fraud prediction.

This project demonstrates the complete Machine Learning workflow, from data preprocessing and exploratory data analysis (EDA) to model training, evaluation, and deployment using a production-ready pipeline.

---

## 🚀 Features

- Exploratory Data Analysis (EDA)
- Data preprocessing and feature engineering
- Handling categorical features using Scikit-learn Pipeline
- Model training using multiple classification algorithms
- Model comparison using evaluation metrics
- Hyperparameter tuning
- Feature Importance visualization
- ROC Curve and Precision-Recall Curve analysis
- Production-ready model serialization using Joblib
- Prediction script for real-time fraud detection
- Backend-ready ML model for API integration

---

## 🛠️ Tech Stack

### Programming Language
- Python 3.x

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

### Machine Learning Models
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## 📂 Dataset

The dataset contains credit card transaction records with features such as:

- Transaction Amount
- Transaction Hour
- Merchant Category
- Foreign Transaction
- Location Mismatch
- Device Trust Score
- Transaction Velocity (Last 24 Hours)
- Cardholder Age
- Fraud Label (Target Variable)

**Target Variable**

- `is_fraud`
  - 0 → Legitimate Transaction
  - 1 → Fraudulent Transaction

---

## 📊 Project Workflow

### 1. Data Collection

- Load dataset
- Explore data structure

### 2. Exploratory Data Analysis

- Dataset information
- Missing value analysis
- Class distribution
- Correlation analysis
- Data visualization

### 3. Data Preprocessing

- Feature selection
- Handling categorical variables
- Train-test split
- Data transformation using Scikit-learn Pipeline

### 4. Model Training

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest

### 5. Model Evaluation

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

### 6. Hyperparameter Tuning

Random Forest model was optimized to improve overall prediction performance.

### 7. Model Deployment

The final trained pipeline is saved as:

```
model/best_model.pkl
```

This model is used for real-time predictions through the backend API.

---

# 📈 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | **99.70%** |
| Precision | **100%** |
| Recall | **80%** |
| F1 Score | **88.89%** |
| ROC-AUC | **1.00** |

> **Note:** Results are based on the current dataset used in this project.

---

## 📁 Project Structure

```
Credit-Card-Fraud-Detection/
│
├── backend/
├── frontend/
├── dataset/
│   └── credit_card_fraud_10k.csv
│
├── model/
│   └── best_model.pkl
│
├── notebooks/
│   └── fraud_detection.ipynb
│
├── predict.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/CHARVI2309/Credit-Card-Fraud-Detection.git
```

Move into the project directory:

```bash
cd Credit-Card-Fraud-Detection
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Train the Model

```bash
python train_model.py
```

### Predict a Transaction

```bash
python predict.py
```

---

## 📌 Sample Input

```json
{
    "amount": 2500,
    "transaction_hour": 14,
    "merchant_category": "Food",
    "foreign_transaction": 0,
    "location_mismatch": 0,
    "device_trust_score": 92,
    "velocity_last_24h": 3,
    "cardholder_age": 32
}
```

---

## 📌 Sample Output

```json
{
    "prediction": "Legitimate",
    "fraud_probability": 0.005
}
```

---

## 📊 Evaluation Metrics Used

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- Feature Importance
- ROC Curve
- Precision-Recall Curve

---

## 🔮 Future Enhancements

- XGBoost and LightGBM implementation
- Deep Learning-based fraud detection
- Real-time transaction monitoring
- Streamlit dashboard
- REST API using FastAPI
- Docker containerization
- Cloud deployment (AWS/Azure/GCP)
- Continuous model retraining
- Explainable AI using SHAP/LIME

---

## 👥 Team Members

- **Charvi Mathur** – Machine Learning
- **Hardi Malviya** – API Development
- **Ayush Khandelwal** – User Interface

---

## 📚 Learning Outcomes

Through this project, we gained practical experience in:

- Data preprocessing
- Feature engineering
- Handling categorical variables
- Binary classification
- Model evaluation
- Machine Learning pipelines
- Model deployment
- Git and GitHub collaboration
- Team-based software development

---

## 📄 License

This project is developed for educational and learning purposes.

---

## ⭐ Acknowledgements

- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Kaggle (Dataset Inspiration)

---

**If you found this project helpful, consider giving it a ⭐ on GitHub!**