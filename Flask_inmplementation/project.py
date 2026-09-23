# Day 1 - API Foundation
import uuid
from flask import request, jsonify

from flask import Flask, jsonify

app = Flask(__name__)

# Starting data structure: 2 categories with 5 questions each (Minimum Requirement)
QUESTIONS = {
    "General Knowledge": [
        {"id": 1, "question": "What is the capital of France?", "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"}, "answer": "C"},
        {"id": 2, "question": "Which planet is known as the Red Planet?", "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Saturn"}, "answer": "B"},
        {"id": 3, "question": "Who wrote 'Romeo and Juliet'?", "options": {"A": "Charles Dickens", "B": "William Shakespeare", "C": "Mark Twain", "D": "Jane Austen"}, "answer": "B"},
        {"id": 4, "question": "What is the largest ocean on Earth?", "options": {"A": "Atlantic", "B": "Indian", "C": "Arctic", "D": "Pacific"}, "answer": "D"},
        {"id": 5, "question": "How many days are in a leap year?", "options": {"A": "365", "B": "366", "C": "364", "D": "367"}, "answer": "B"}
    ],
    "Science": [
        {"id": 6, "question": "What is the chemical symbol for water?", "options": {"A": "CO2", "B": "H2O", "C": "O2", "D": "NaCl"}, "answer": "B"},
        {"id": 7, "question": "What force keeps us on the ground?", "options": {"A": "Gravity", "B": "Magnetism", "C": "Friction", "D": "Inertia"}, "answer": "A"},
        {"id": 8, "question": "Which gas do plants absorb from the atmosphere?", "options": {"A": "Oxygen", "B": "Nitrogen", "C": "Carbon Dioxide", "D": "Hydrogen"}, "answer": "C"},
        {"id": 9, "question": "What is the hardest natural substance on Earth?", "options": {"A": "Gold", "B": "Iron", "C": "Diamond", "D": "Quartz"}, "answer": "C"},
        {"id": 10, "question": "How many teeth does an adult human normally have?", "options": {"A": "32", "B": "28", "C": "30", "D": "34"}, "answer": "A"}
    ]
}

QUIZZES = {}

# 1. Welcome Endpoint (GET /)
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({
        "message": "Welcome to the Quiz-Game API"
    })

# 2. Categories Endpoint (GET /categories)
@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify({
        "categories": list(QUESTIONS.keys())
    })

# 3. Category Detail Endpoint (GET /categories/<category_name>)
@app.route('/categories/<category_name>', methods=['GET'])
def get_category(category_name):
    # Make a lowercase lookup map so typing 'science' or 'Science' both work
    normalized_questions = {k.lower(): (k, v) for k, v in QUESTIONS.items()}
    search_key = category_name.lower()
    
    if search_key in normalized_questions:
        original_name, questions_list = normalized_questions[search_key]
        return jsonify({
            "category": original_name,
            "total_questions": len(questions_list),
            "questions": questions_list
        })
    
    # Return a 404 error if the category doesn't exist
    return jsonify({"error": "Category Not Found"}), 404

#day 2 - The start of the quiz
@app.route("/quiz/start", methods=["POST"])
def start_quiz():
    #1. recieve and safely translate incoming json data sent by the user or player idk
    body = request.get_json() or {}
    category_input = body.get("category")
    num_questions_requested = body.get("number_of_questions")

    #this code makes sure that they are included in both fields
    if not category_input or num_questions_requested is None:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    #2. checks if the category of questions exist by using case insensitive searching
    cats = {k.lower(): k for k in QUESTIONS.keys()}
    if category_input.lower() not in cats:
        return jsonify({
            "error": "invalid category my good sir",
            "message": f"{category_input} does not exist"
        }), 404

    official_cat = cats[category_input.lower()]
    available_q_list = QUESTIONS[official_cat]

    #this code makes sure they arent asking for to many questions
    if num_questions_requested <= 0 or num_questions_requested > len(available_q_list):
        return jsonify({
            "error": "invalid question count",
            "message": f"Choose between one and {len(available_q_list)} questions."
        }), 400

    #3 create a new id everytime u restart the quiz for safety purposes
    quiz_id = str(uuid.uuid4())

    #4 save the game parameters in our tracker"i am sure thats later in the code"
    QUIZZES[quiz_id] = {
        "category": official_cat,
        "total_questions": num_questions_requested,
        "questions": available_q_list[:num_questions_requested]
    }

    return jsonify({
        "quiz_id": quiz_id,
        "category": official_cat,
        "total_questions": num_questions_requested,
        "score": 0,
        "strikes": 0,
        "questions_answerd": 0,
        "question_pool": available_q_list[:num_questions_requested]  # they get the amount they requested
    })
    #5(final day 2 part) Returns success info
    return jsonify({
        "message": "Quiz started",
        "quiz_id": quiz_id,
        "category": official_cat,
        "total_questions": num_questions_requested
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
    
