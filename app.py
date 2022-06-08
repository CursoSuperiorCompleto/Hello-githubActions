from flask import Flask

app = Flask(__name__)

@app.route("/docker")
def hello_world():
    return "<p> Hey, I'm Docker! It's a pleasure </p>"

@app.route("/python")
def who_am_i():
    return "<h1> HEEEEEEEEEEEEEEEEEEEEEY, DO YOU ALREADY KNOW ME?? </h1>"

@app.route("/spark")
def get_users():
    return "<h1> Hahah, i'm the BEST! </h1>"