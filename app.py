from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    time_now = time.time()
    return render_template("index.html", time_now=time_now)


@app.route("/about_me")
def about_me():
    user = "Nejc"
    return render_template("about_me.html", user=user)


@app.route("/portfolio")
def portfolio():
    projects = [
        {
            "name": "Test",
            "year": 2018
         },
        {
            "name": "Fitness",
            "year": 2019
        },
        {
            "name": "Carpark",
            "year": 2016
        }
    ]
    return render_template("portfolio.html", projects=projects)


if __name__ == "__main__":
    app.run(debug=True)