import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("Employee Performance.csv")

# Drop unnecessary columns
df.drop(["EmployeeNumber", "EmployeeCount", "StandardHours", "Over18"], axis=1, inplace=True)

# Create target (Performance Rating 🔥)
df["PerformanceRating"] = df["MonthlyIncome"].apply(
    lambda x: 1 if x < 3000 else (2 if x < 6000 else 3)
)

# Handle missing values
df.fillna(method="ffill", inplace=True)

# Encode categorical columns
le = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = le.fit_transform(df[col])

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Features & target
X = df.drop("PerformanceRating", axis=1)
y = df["PerformanceRating"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Employee Performance Model Trained!")