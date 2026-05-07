from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    return render_template("predict.html", prediction="")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)