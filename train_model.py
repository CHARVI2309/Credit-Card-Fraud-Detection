import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report
)
df = pd.read_csv("dataset/credit_card_fraud_10k.csv")
X = df.drop(["transaction_id", "is_fraud"], axis=1)
y = df["is_fraud"]
categorical_features = [
    "merchant_category"
]
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier",
        RandomForestClassifier(
            n_estimators=200,
            random_state=42
        )
    )
])
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

y_prob = pipeline.predict_proba(X_test)[:,1]
print("Accuracy :", accuracy_score(y_test,y_pred))
print("Precision:", precision_score(y_test,y_pred))
print("Recall   :", recall_score(y_test,y_pred))
print("F1 Score :", f1_score(y_test,y_pred))
print("ROC-AUC  :", roc_auc_score(y_test,y_prob))

print(classification_report(y_test,y_pred))
joblib.dump(
    pipeline,
    "model/best_model.pkl"
)

print("Model saved successfully!")