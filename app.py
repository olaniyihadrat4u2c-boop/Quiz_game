#contains the app
from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "yokoso wathisno no soul society"