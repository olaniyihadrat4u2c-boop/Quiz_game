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
def get_anime():
    return anime



@app.route("/books",methods=["POST"])
def create_book():
    data=request.json

    books.append(data)

    return{
        "message":"Book received",
        "book": data
    },201

cool = []


# 1. Add "PUT" to the allowed methods array
@app.route("/cool", methods=["POST", "PUT"])
def create_cool():
    data = request.json
    
    # 2. Check if the incoming request is a PUT request
    if request.method == "PUT":
        # Add your code here to update the resource instead of appending it
        return {
            "dialoge": "updated successfully",
            "random": data
        }, 200 # 200 OK is standard for updates

    # Your original POST logic remains here
    cool.append(data)
    return {
        "dialoge": "rlly dude",
        "random": data
    }, 201
