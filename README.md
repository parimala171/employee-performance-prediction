# 👨‍💼 Employee Performance Prediction System

## 📌 Project Overview

This project is an end-to-end **Employee Performance Prediction System** that uses Machine Learning to predict employee performance levels based on HR data.

The system includes:

* Data preprocessing & feature engineering
* Machine Learning model
* Flask API for real-time predictions
* Simulated streaming for production-like behavior

---

## 🚀 Features

* 📊 Data cleaning & preprocessing
* 🧠 Feature engineering (Experience Level, Performance Rating)
* 🤖 Machine Learning model (RandomForest)
* 🌐 Flask API for prediction
* 📡 Real-time simulation using streaming
* 📈 Exploratory Data Analysis (EDA)

---

## 📂 Project Structure

```
EMPLOYEE_PERFORMANCE_SYSTEM/
│
├── Employee Performance.csv   # Raw dataset (not included in repo)
├── cleaned_data.csv           # Processed dataset
├── retrain.py                 # Model training script
├── model.pkl                  # Trained ML model
├── stream_data.py             # Simulated streaming data
├── app.py                     # Flask API
├── employee_analysis.ipynb    # EDA & visualization
├── Dockerfile
└── requirements.txt
```

---

## 📥 Dataset

Dataset is not uploaded due to GitHub size limits.

👉 Download from:
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

👉 After downloading, rename and place as:

```
Employee Performance.csv
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 🧠 Model Training

```bash
python retrain.py
```

---

## 🌐 Run Flask API

```bash
python app.py
```

👉 Open in browser:

```
http://127.0.0.1:5004
```

---

## 📡 Real-time Simulation

```bash
python stream_data.py
```

---

## 🧪 Sample API Request

```json
POST /predict
{
  "Age": 35,
  "MonthlyIncome": 5000,
  "TotalWorkingYears": 10
}
```

👉 Response:

```json
{
  "Predicted Rating": "Medium Performance"
}
```

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Flask
* Machine Learning
* Docker (optional)

---

## 🔥 Key Learnings

* Data preprocessing & feature engineering
* Handling categorical data
* Building ML classification model
* Deploying ML model using Flask API
* Simulating real-time prediction systems
* Managing projects using Git & GitHub

---

## ⚠️ Notes

* Large dataset files are excluded using `.gitignore`
* Only essential project files are uploaded

---

## 👨‍💻 Author

**Parimala.S**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
