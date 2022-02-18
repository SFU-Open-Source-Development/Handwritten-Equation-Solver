from flask import Flask, render_template, url_for, redirect,request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './Uploads'
ALLOWED_EXTENSIONS = { 'pdf', 'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/app")
def apP():
    return render_template("app.html")


@app.route("/prs",methods=["POST"])
def prcs():
    image = request.files["image"]

app.run(debug=True)
