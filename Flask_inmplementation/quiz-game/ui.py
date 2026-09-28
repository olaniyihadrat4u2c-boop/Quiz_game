from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

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

# ========== PAGES ==========

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/categories')
def categories_page():
    return render_template('categories.html')

@app.route('/quiz')
def quiz_page():
    return render_template('quiz.html')

@app.route('/result')
def result_page():
    return render_template('result.html')

# ========== API ==========

@app.route('/api/categories', methods=['GET'])
def get_categories():
    return jsonify({"categories": list(QUESTIONS.keys())})

@app.route('/api/quiz/start', methods=['POST'])
def start_quiz():
    data = request.get_json() or {}
    category = data.get("category")
    num = data.get("number_of_questions")

    if not category or num is None:
        return jsonify({"error": "Missing category or number_of_questions"}), 400

    try:
        num = int(num)
    except:
        return jsonify({"error": "number_of_questions must be a number"}), 400

    cats = {k.lower(): k for k in QUESTIONS}
    if category.lower() not in cats:
        return jsonify({"error": "Category not found"}), 404

    official = cats[category.lower()]
    available = QUESTIONS[official]

    if num < 1 or num > len(available):
        return jsonify({"error": f"Choose between 1 and {len(available)} questions"}), 400

    quiz_id = str(uuid.uuid4())
    QUIZZES[quiz_id] = {
        "category": official,
        "questions": available[:num],
        "total_questions": num,
        "current_index": 0,
        "score": 0,
        "strikes": 0,
        "completed": False
    }

    return jsonify({
        "quiz_id": quiz_id,
        "category": official,
        "total_questions": num,
        "score": 0,
        "strikes": 0
    }), 201

@app.route('/api/quiz/<quiz_id>/question', methods=['GET'])
def get_question(quiz_id):
    quiz = QUIZZES.get(quiz_id)
    if not quiz:
        return jsonify({"error": "Quiz not found"}), 404

    if quiz["completed"] or quiz["strikes"] >= 3 or quiz["current_index"] >= quiz["total_questions"]:
        quiz["completed"] = True
        return jsonify({"message": "Quiz over", "reason": "Quiz finished or 3 strikes"}), 400

    q = quiz["questions"][quiz["current_index"]]
    return jsonify({
        "question_number": quiz["current_index"] + 1,
        "total_questions": quiz["total_questions"],
        "question": q["quest=+ion"],
        "options": q["options"],
        "score": quiz["score"],
        "strikes": quiz["strikes"]
    })

@app.route('/api/quiz/<quiz_id>/answer', methods=['POST'])
def submit_answer(quiz_id):
    quiz = QUIZZES.get(quiz_id)
    if not quiz:
        return jsonify({"error": "Quiz not found"}), 404
    if quiz["completed"]:
        return jsonify({"error": "Quiz already finished"}), 400

    data = request.get_json() or {}
    answer = data.get("answer")
    if not answer:
        return jsonify({"error": "Missing answer"}), 400

    correct = quiz["questions"][quiz["current_index"]]["answer"]
    is_correct = answer.upper() == correct.upper()

    if is_correct:
        quiz["score"] += 1
    else:
        quiz["strikes"] += 1

    quiz["current_index"] += 1

    if quiz["strikes"] >= 3 or quiz["current_index"] >= quiz["total_questions"]:
        quiz["completed"] = True

    return jsonify({
        "correct": is_correct,
        "score": quiz["score"],
        "strikes": quiz["strikes"],
        "completed": quiz["completed"]
    })

@app.route('/api/quiz/<quiz_id>/result', methods=['GET'])
def get_result(quiz_id):
    quiz = QUIZZES.get(quiz_id)
    if not quiz:
        return jsonify({"error": "Quiz not found"}), 404

    total = quiz["total_questions"]
    score = quiz["score"]
    percentage = round((score / total) * 100) if total > 0 else 0

    return jsonify({
        "score": score,
        "total_questions": total,
        "percentage": percentage,
        "strikes": quiz["strikes"],
        "completed": quiz["completed"]
    })

if __name__ == '__main__':
    app.run(debug=True)
