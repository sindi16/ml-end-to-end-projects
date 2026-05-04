from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import pickle

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model("model/btc_lstm_model.keras")

# Load scaler
with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

WINDOW_SIZE = 1440
FEATURES = 6

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Example: user sends last window as input (for simplicity demo)
        data = request.json["data"]

        data = np.array(data).reshape(WINDOW_SIZE, FEATURES)

        # scale
        data_scaled = scaler.transform(data)

        # reshape for LSTM
        X = data_scaled.reshape(1, WINDOW_SIZE, FEATURES)

        prediction = model.predict(X)[0][0]

        return {"prediction": float(prediction)}

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    app.run(debug=True)