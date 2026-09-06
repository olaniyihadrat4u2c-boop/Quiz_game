#contains the app
from flask import Flask, request

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

books = [
    {"id":1, "title": "Python Basics"},
    {"id": 2, "title": "Learning HTML"},
    {"id": 3, "title": "Introduction to science"}
]
@app.route("/books",methods=["GET"])
def get_books():
    return books

anime = [
    {"name": "gojo", "rank": 1, "title": "the strongest of today", "arc": "shibuya incident"},
    {"name": "sukuna", "rank": 2, "title": "the strongest in history", "arc": "shinjuku showdown"},
    {"name": "modulo yuji", "rank": 3, "title": "the strongest of tommorow", "arc": "2 eye camility"},
]
@app.route("/anime",methods=["GET"])
def get_anome():
    return anime

@app.route("/books",methods=["POST"])
def create_book():
    data=request.json

    return{
        "message":"Book received",
        "book": data
    },201