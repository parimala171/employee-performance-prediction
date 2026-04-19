from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Employee Performance API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = list(data.values())
    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)[0]

    rating = {
        1: "Low Performance",
        2: "Medium Performance",
        3: "High Performance"
    }

    return jsonify({
        "Predicted Rating": rating[int(prediction)]
    })

if __name__ == "__main__":
    app.run(debug=True, port=5004)