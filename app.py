from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hey, there! What's up? </p>"

@app.route("/users")
def get_users():
    return "<h1> Imagine a json returning right here! </h1>"