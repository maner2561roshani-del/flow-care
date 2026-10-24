from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    name = request.form["name"]
    age = request.form["age"]
    last_period = request.form["last_period"]

    date = datetime.strptime(last_period, "%Y-%m-%d")
    next_date = date + timedelta(days=28)

    return render_template(
        "result.html",
        name=name,
        age=age,
        next_date=next_date.strftime("%d-%m-%Y")
    )

if __name__ == "__main__":
    app.run(debug=True)