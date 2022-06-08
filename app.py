from flask import Flask

app = Flask(__name__)

@app.route("/docker")
def hello_world():
    return "<p> HEY, MY NAME IS DOCKER! </p>"

@app.route("/python")
def who_am_i():
    return "<h1> HEEEEEEEEEEEEEEEEEEEEEY, DO YOU ALREADY KNOW ME?? </h1>"

@app.route("/spark")
def get_users():
    return "<h1> WHAT'S UP, GUYS? I'M SPARK! </h1>"