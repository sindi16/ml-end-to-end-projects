from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# load EXACT same objects from training
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
model = joblib.load("models/kmeans_tfidf.pkl")

cluster_names = {
    0: "sport",
    1: "business",
    2: "politics",
    3: "tech",
    4: "entertainment"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["text"]

    # safety check
    if not text.strip():
        return render_template("index.html", prediction="Empty input")

    X = vectorizer.transform([text])

    cluster = model.predict(X)[0]
    category = cluster_names.get(cluster, "unknown")

    return render_template(
        "index.html",
        prediction=category,
        cluster=cluster
    )

if __name__ == "__main__":
    app.run(debug=True)