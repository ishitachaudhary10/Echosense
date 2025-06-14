import pickle
import os
import cv2
import mediapipe as mp
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
# Dataset Path
data_dir = r'C:\Users\DeLL\Downloads\archive\asl_dataset_train'

# Mediapipe Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.9)

print("Loading dataset...")

data = []
labels = []
label_encoder = LabelEncoder()

for label in sorted(os.listdir(data_dir)):
    if label == '.DS_Store':  
        continue  
    print(f"Processing label: {label}")
    
    label_path = os.path.join(data_dir, label)
    for img_file in os.listdir(label_path):
        img_path = os.path.join(label_path, img_file)
        img = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        results = hands.process(img_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Normalize coordinates
                x_vals = [lm.x for lm in hand_landmarks.landmark]
                y_vals = [lm.y for lm in hand_landmarks.landmark]
                z_vals = [lm.z for lm in hand_landmarks.landmark]
                
                min_x, max_x = min(x_vals), max(x_vals)
                min_y, max_y = min(y_vals), max(y_vals)
                
                normalized_data = []
                for i in range(21):
                    normalized_x = (x_vals[i] - min_x) / (max_x - min_x)
                    normalized_y = (y_vals[i] - min_y) / (max_y - min_y)
                    normalized_z = z_vals[i]  
                    normalized_data.extend([normalized_x, normalized_y, normalized_z])
                
                data.append(normalized_data)
                labels.append(label)

X = np.array(data)
y = np.array(labels)
y = label_encoder.fit_transform(y)

if len(X) == 0:
    raise ValueError("Dataset is empty! Please check the data folder path or image processing.")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
print("Training the model...")
model = xgb.XGBClassifier(n_estimators=150, max_depth=5, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# Save Model and Label Encoder
with open("sign_language_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)
with open("X_test.pkl", "wb") as f:
    pickle.dump(X_test, f)
with open("y_test.pkl", "wb") as f:
    pickle.dump(y_test, f)

print("Model trained and saved as 'sign_language_model.pkl'!")




