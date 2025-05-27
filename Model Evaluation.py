import pickle
import numpy as np
import xgboost as xgb
from sklearn.metrics import confusion_matrix, classification_report

# Load Model and Encoders
with open("sign_language_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)
with open("X_test.pkl", "rb") as f:
    X_test = pickle.load(f)
with open("y_test.pkl", "rb") as f:
    y_test = pickle.load(f)

y_pred = model.predict(X_test)

# Convert to Original Labels
y_test_labels = label_encoder.inverse_transform(y_test)
y_pred_labels = label_encoder.inverse_transform(y_pred)

# Confusion Matrix with Correct Order
labels = sorted(set(y_test_labels))  
conf_matrix = confusion_matrix(y_test_labels, y_pred_labels, labels=labels)
print("Confusion Matrix:")
print(conf_matrix)

print("\nClassification Report:")
print(classification_report(y_test_labels, y_pred_labels))







