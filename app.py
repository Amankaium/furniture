from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("all_furniture.html")

@app.route("/kitchen")
def kitchen():
    return render_template("kitchen.html")

@app.route("/winner/<name>")
def winner(name):
    name = name.capitalize()
    return render_template("winner.html", name=name)
