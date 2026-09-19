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

# Pre-populated list of magical books
books = [
    {"id": 1, "title": "Python Basics", "author": "Unknown"},
    {"id": 2, "title": "Learning HTML", "author": "Unknown"},
    {"id": 3, "title": "Introduction to science", "author": "Unknown"}
]

@app.route("/books", methods=["GET"])
def get_books():
    return books

# Anime tier list database
anime = [
    {"name": "gojo", "rank": 1, "title": "the strongest of today", "arc": "shibuya incident"},
    {"name": "sukuna", "rank": 2, "title": "the strongest in history", "arc": "shinjuku showdown"},
    {"name": "modulo yuji", "rank": 3, "title": "the strongest of tommorow", "arc": "2 eye camility"},
]

@app.route("/anime", methods=["GET"])
def get_anime():
    return anime

@app.route("/books", methods=["POST"])
def create_book():
    data = request.json
    books.append(data)
    return {
        "message": "Domain Expansion: Infinite Books! Your book has been successfully manifested into existence.",
        "book": data
    }, 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.json or {}
    
    if "title" not in data:
        return {"message": "Baka! You can't overwrite a book without giving me a 'title' first."}, 400

    for book in books:
        if book["id"] == book_id:
            book["title"] = data["title"]
            if "author" in data:
                book["author"] = data["author"]
            
            return {
                "message": "Yeah this a magical book that puts new words every month or so deal with it mate u bought it",
                "book": book
            }, 200

    return {"message": "You thought you found the book? Throughout heaven and earth, that ID alone is non-existent. 404!"}, 404

@app.route("/books/<int:book_id>", methods=["PATCH"])
def patch_book(book_id):
    data = request.json or {}

    for book in books:
        if book["id"] == book_id:
            if "title" in data:
                book["title"] = data["title"]
            if "author" in data:
                book["author"] = data["author"]
                
            return {
                "message": "oh the magical book only put allitle bit of information mate guess you gotta wait",
                "book": book
            }, 200
            
    return {"message": "Stand proud, you are strong... but your book data is lost in the Grand Line. 404!"}, 404

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {
                "message": "Yeah the magical books been erased frome existance mate u didnt do the right thing mate"
            }
            
    return {"message": "Are you the book because you're 404, or are you 404 because you've been completely erased by Hollow Purple?"}, 404

if __name__ == "__main__":
    app.run(debug=True)
