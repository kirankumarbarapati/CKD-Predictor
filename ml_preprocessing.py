# We will rename this file to train_model.py after this step

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
# Import new tools for Phase 3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# --- Phase 2 Code (Data Loading and Cleaning) ---

file_path = 'kidney_disease.csv'
try:
    df = pd.read_csv(file_path, na_values='?')
    print("SUCCESS: Dataset loaded successfully!")
except FileNotFoundError:
    print(f"ERROR: File '{file_path}' not found.")
    exit()

# Drop 'id'
df.drop('id', axis=1, inplace=True)

# Correct data types
for col in ['pcv', 'wc', 'rc']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Clean classification column
df['classification'] = df['classification'].str.strip()

# Impute missing values
all_cols = df.columns
numerical_cols = df.select_dtypes(include=np.number).columns
categorical_cols = [col for col in all_cols if col not in numerical_cols]

for col in numerical_cols:
    df[col].fillna(df[col].mean(), inplace=True)
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Encode Categorical Features
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])


# --- START OF NEW PHASE 3 CODE ---

print("\n--- Starting Phase 3: Model Training ---\n")

# 1. Split Data into Features (X) and Target (y)
# X contains all columns except 'classification'
X = df.drop('classification', axis=1)
# y contains only the 'classification' column
y = df['classification']

# Split into training and testing sets (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Data split into training and testing sets.")
print(f"Training set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")

# 2. Train a RandomForestClassifier Model
print("\nTraining the RandomForestClassifier model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model training complete.")

# 3. Evaluate the Model
print("\nEvaluating the model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy on Test Data: {accuracy * 100:.2f}%")

# 4. Save the Trained Model
model_filename = 'ckd_model.joblib'
joblib.dump(model, model_filename)
print(f"\nModel saved successfully as '{model_filename}'")

