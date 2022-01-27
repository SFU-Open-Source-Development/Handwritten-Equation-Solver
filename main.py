from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/about")
def about():
    return render_template("about.html")


app.run(debug=True)
