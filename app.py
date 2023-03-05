from flask import Flask

app = Flask(__name__)

@app.route("/hering")
def hello_world():
    return "<p> Fellipe Fernandes and Felipe Ferraz! </p>"

@app.route("/arcellor")
def who_am_i():
    return "<h1> Jonathan e Ketlen </h1>"

@app.route("/portobello")
def get_users():
    return "<h1> Magnum, Lucas e Luan </h1>"