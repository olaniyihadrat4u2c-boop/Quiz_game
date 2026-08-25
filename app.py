#contains the app
from flask import Flask

#um random thing i think it allows the thing to like route and bring you the thing i dont really know 
app = Flask(__name__)

#these are the different routes
@app.route("/")
def home():
    return "orewa monkey d luffy"

@app.route("/about")
def about():
    return "kaitoku shizen"

@app.route("/contact")
def contact():
    return "orewa dev_cocalee i'l become the king of coders"