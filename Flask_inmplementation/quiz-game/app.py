from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import uuid
import random

app = Flask(__name__)
CORS(app)

# ============================================================
# QUESTION BANK
# ============================================================

QUESTIONS = {
    "General Knowledge": [
        {"id": 1,  "question": "What is the capital of France?", "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"}, "answer": "C"},
        {"id": 2,  "question": "Which planet is known as the Red Planet?", "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Saturn"}, "answer": "B"},
        {"id": 3,  "question": "Who wrote 'Romeo and Juliet'?", "options": {"A": "Charles Dickens", "B": "William Shakespeare", "C": "Mark Twain", "D": "Jane Austen"}, "answer": "B"},
        {"id": 4,  "question": "What is the largest ocean on Earth?", "options": {"A": "Atlantic", "B": "Indian", "C": "Arctic", "D": "Pacific"}, "answer": "D"},
        {"id": 5,  "question": "How many days are in a leap year?", "options": {"A": "365", "B": "366", "C": "364", "D": "367"}, "answer": "B"},
        {"id": 6,  "question": "Which country has the most time zones?", "options": {"A": "USA", "B": "Russia", "C": "France", "D": "China"}, "answer": "C"},
        {"id": 7,  "question": "What is the tallest mountain in the world?", "options": {"A": "K2", "B": "Kangchenjunga", "C": "Mount Everest", "D": "Lhotse"}, "answer": "C"},
        {"id": 8,  "question": "Which animal is featured on the logo of Ferrari?", "options": {"A": "Horse", "B": "Bull", "C": "Lion", "D": "Eagle"}, "answer": "A"},
    ],

    "Science": [
        {"id": 10, "question": "What is the chemical symbol for water?", "options": {"A": "CO2", "B": "H2O", "C": "O2", "D": "NaCl"}, "answer": "B"},
        {"id": 11, "question": "What force keeps us on the ground?", "options": {"A": "Gravity", "B": "Magnetism", "C": "Friction", "D": "Inertia"}, "answer": "A"},
        {"id": 12, "question": "Which gas do plants absorb from the atmosphere?", "options": {"A": "Oxygen", "B": "Nitrogen", "C": "Carbon Dioxide", "D": "Hydrogen"}, "answer": "C"},
        {"id": 13, "question": "What is the hardest natural substance on Earth?", "options": {"A": "Gold", "B": "Iron", "C": "Diamond", "D": "Quartz"}, "answer": "C"},
        {"id": 14, "question": "How many teeth does an adult human normally have?", "options": {"A": "32", "B": "28", "C": "30", "D": "34"}, "answer": "A"},
        {"id": 15, "question": "What is the speed of light (approx)?", "options": {"A": "300,000 km/s", "B": "150,000 km/s", "C": "30,000 km/s", "D": "3,000 km/s"}, "answer": "A"},
        {"id": 16, "question": "Which planet has the most moons?", "options": {"A": "Jupiter", "B": "Saturn", "C": "Uranus", "D": "Neptune"}, "answer": "B"},
        {"id": 17, "question": "DNA stands for…", "options": {"A": "Deoxyribonucleic Acid", "B": "Dinucleic Acid", "C": "Dextrose Nucleic Acid", "D": "Double Nucleic Acid"}, "answer": "A"},
    ],

    "Technology": [
        {"id": 20, "question": "Who co-founded Apple with Steve Jobs?", "options": {"A": "Bill Gates", "B": "Steve Wozniak", "C": "Elon Musk", "D": "Mark Zuckerberg"}, "answer": "B"},
        {"id": 21, "question": "What does 'HTTP' stand for?", "options": {"A": "HyperText Transfer Protocol", "B": "High Transfer Text Protocol", "C": "Hyperlink Text Transfer Process", "D": "Home Tool Transfer Protocol"}, "answer": "A"},
        {"id": 22, "question": "Which company developed the Android OS?", "options": {"A": "Apple", "B": "Microsoft", "C": "Google", "D": "Samsung"}, "answer": "C"},
        {"id": 23, "question": "What is the name of Elon Musk's brain-chip company?", "options": {"A": "OpenAI", "B": "Neuralink", "C": "SpaceX", "D": "Tesla AI"}, "answer": "B"},
        {"id": 24, "question": "In programming, what does 'CPU' stand for?", "options": {"A": "Central Processing Unit", "B": "Computer Personal Unit", "C": "Core Power Utility", "D": "Central Program Unit"}, "answer": "A"},
        {"id": 25, "question": "Which language is primarily used for iOS apps?", "options": {"A": "Java", "B": "Swift", "C": "Kotlin", "D": "C#"}, "answer": "B"},
        {"id": 26, "question": "What year was the first iPhone released?", "options": {"A": "2005", "B": "2007", "C": "2009", "D": "2010"}, "answer": "B"},
        {"id": 27, "question": "What does 'AI' stand for?", "options": {"A": "Automated Intelligence", "B": "Artificial Intelligence", "C": "Advanced Interface", "D": "Applied Informatics"}, "answer": "B"},
    ],

    "Movies & TV": [
        {"id": 30, "question": "In The Matrix, what color pill does Neo take?", "options": {"A": "Blue", "B": "Red", "C": "Green", "D": "Yellow"}, "answer": "B"},
        {"id": 31, "question": "Which movie features the line 'I am your father'?", "options": {"A": "Star Trek", "B": "Star Wars", "C": "Blade Runner", "D": "Dune"}, "answer": "B"},
        {"id": 32, "question": "Who directed Inception?", "options": {"A": "Steven Spielberg", "B": "Christopher Nolan", "C": "James Cameron", "D": "Ridley Scott"}, "answer": "B"},
        {"id": 33, "question": "What is the name of the coffee shop in Friends?", "options": {"A": "Central Perk", "B": "Monk's Cafe", "C": "Luke's Diner", "D": "MacLaren's"}, "answer": "A"},
        {"id": 34, "question": "In Breaking Bad, what is Walter White's street name?", "options": {"A": "Heisenberg", "B": "The Cook", "C": "Blue Magic", "D": "Mr. White"}, "answer": "A"},
        {"id": 35, "question": "Which Marvel movie first featured Spider-Man in the MCU?", "options": {"A": "Spider-Man: Homecoming", "B": "Captain America: Civil War", "C": "Avengers: Infinity War", "D": "Iron Man 3"}, "answer": "B"},
        {"id": 36, "question": "What is the highest-grossing film of all time (as of 2024)?", "options": {"A": "Avengers: Endgame", "B": "Avatar", "C": "Titanic", "D": "Star Wars: The Force Awakens"}, "answer": "B"},
        {"id": 37, "question": "In Game of Thrones, who said 'Winter is Coming'?", "options": {"A": "Tyrion Lannister", "B": "Jon Snow", "C": "Ned Stark", "D": "Daenerys"}, "answer": "C"},
    ],

    "Video Games": [
        {"id": 40, "question": "What is the best-selling video game of all time?", "options": {"A": "Minecraft", "B": "GTA V", "C": "Tetris", "D": "Wii Sports"}, "answer": "A"},
        {"id": 41, "question": "In which game do you collect Chaos Emeralds?", "options": {"A": "Mario", "B": "Sonic the Hedgehog", "C": "Crash Bandicoot", "D": "Spyro"}, "answer": "B"},
        {"id": 42, "question": "What does 'NPC' stand for?", "options": {"A": "Non-Playable Character", "B": "New Player Class", "C": "Network Protocol Code", "D": "Next Phase Checkpoint"}, "answer": "A"},
        {"id": 43, "question": "Which company makes the PlayStation?", "options": {"A": "Microsoft", "B": "Nintendo", "C": "Sony", "D": "Sega"}, "answer": "C"},
        {"id": 44, "question": "In Fortnite, what is the name of the battle bus?", "options": {"A": "Battle Bus", "B": "Drop Ship", "C": "Sky Carrier", "D": "It has no special name"}, "answer": "A"},
        {"id": 45, "question": "What year was the original Pokémon Red/Blue released in Japan?", "options": {"A": "1994", "B": "1996", "C": "1998", "D": "2000"}, "answer": "B"},
        {"id": 46, "question": "Which game popularized the battle royale genre?", "options": {"A": "Fortnite", "B": "PUBG", "C": "Apex Legends", "D": "Call of Duty"}, "answer": "B"},
        {"id": 47, "question": "What is the main character's name in The Legend of Zelda?", "options": {"A": "Zelda", "B": "Link", "C": "Ganon", "D": "Impa"}, "answer": "B"},
    ],

    "Space": [
        {"id": 50, "question": "How many planets are in our solar system?", "options": {"A": "7", "B": "8", "C": "9", "D": "10"}, "answer": "B"},
        {"id": 51, "question": "What is the closest star to Earth (besides the Sun)?", "options": {"A": "Alpha Centauri", "B": "Betelgeuse", "C": "Sirius", "D": "Proxima Centauri"}, "answer": "D"},
        {"id": 52, "question": "Who was the first human in space?", "options": {"A": "Neil Armstrong", "B": "Yuri Gagarin", "C": "Buzz Aldrin", "D": "John Glenn"}, "answer": "B"},
        {"id": 53, "question": "What is a black hole?", "options": {"A": "A dark planet", "B": "A region where gravity is so strong nothing can escape", "C": "An empty area in space", "D": "A collapsed star that becomes a comet"}, "answer": "B"},
        {"id": 54, "question": "Which planet is famous for its rings?", "options": {"A": "Jupiter", "B": "Saturn", "C": "Uranus", "D": "Neptune"}, "answer": "B"},
        {"id": 55, "question": "What is the name of NASA's most famous space telescope (launched 1990)?", "options": {"A": "James Webb", "B": "Hubble", "C": "Spitzer", "D": "Kepler"}, "answer": "B"},
        {"id": 56, "question": "How long does it take light from the Sun to reach Earth?", "options": {"A": "8 minutes", "B": "1 hour", "C": "24 hours", "D": "1 second"}, "answer": "A"},
        {"id": 57, "question": "What galaxy do we live in?", "options": {"A": "Andromeda", "B": "Milky Way", "C": "Whirlpool", "D": "Triangulum"}, "answer": "B"},
    ],

    "Music": [
        {"id": 60, "question": "Which artist is known as the 'King of Pop'?", "options": {"A": "Elvis Presley", "B": "Michael Jackson", "C": "Prince", "D": "Freddie Mercury"}, "answer": "B"},
        {"id": 61, "question": "What band performed 'Bohemian Rhapsody'?", "options": {"A": "The Beatles", "B": "Queen", "C": "Led Zeppelin", "D": "Pink Floyd"}, "answer": "B"},
        {"id": 62, "question": "How many strings does a standard guitar have?", "options": {"A": "4", "B": "5", "C": "6", "D": "7"}, "answer": "C"},
        {"id": 63, "question": "Which streaming platform is owned by Spotify?", "options": {"A": "Apple Music", "B": "Spotify itself", "C": "Tidal", "D": "YouTube Music"}, "answer": "B"},
        {"id": 64, "question": "What year did The Beatles break up?", "options": {"A": "1968", "B": "1970", "C": "1972", "D": "1965"}, "answer": "B"},
        {"id": 65, "question": "Which artist released the album 'Thriller'?", "options": {"A": "Prince", "B": "Michael Jackson", "C": "Madonna", "D": "Whitney Houston"}, "answer": "B"},
        {"id": 66, "question": "What does 'DJ' stand for?", "options": {"A": "Disk Jockey", "B": "Digital Jockey", "C": "Dance Judge", "D": "Dynamic Jazz"}, "answer": "A"},
        {"id": 67, "question": "Which instrument has 88 keys?", "options": {"A": "Organ", "B": "Piano", "C": "Harpsichord", "D": "Synthesizer"}, "answer": "B"},
    ],

    "Internet & Memes": [
        {"id": 70, "question": "What does 'LOL' stand for?", "options": {"A": "Lots of Love", "B": "Laughing Out Loud", "C": "League of Legends", "D": "Look Out Later"}, "answer": "B"},
        {"id": 71, "question": "Which company owns YouTube?", "options": {"A": "Meta", "B": "Amazon", "C": "Google", "D": "Microsoft"}, "answer": "C"},
        {"id": 72, "question": "What year was Twitter (now X) founded?", "options": {"A": "2004", "B": "2006", "C": "2008", "D": "2010"}, "answer": "B"},
        {"id": 73, "question": "What does 'FOMO' mean?", "options": {"A": "Fear Of Missing Out", "B": "Friends Over Money Only", "C": "Full Of Memes Online", "D": "Find Our Main Objective"}, "answer": "A"},
        {"id": 74, "question": "Which animal is the 'doge' meme?", "options": {"A": "Cat", "B": "Shiba Inu", "C": "Corgi", "D": "Husky"}, "answer": "B"},
        {"id": 75, "question": "What is the most-liked tweet of all time (approx)?", "options": {"A": "A celebrity announcement", "B": "Elon Musk's 'next I'm buying Coca-Cola'", "C": "An Obama tweet", "D": "It changes too often to say"}, "answer": "D"},
        {"id": 76, "question": "What does 'NPC' mean in internet slang?", "options": {"A": "Noob Player Character", "B": "Non-Playable Character (someone who follows the crowd)", "C": "New Post Creator", "D": "Never Post Content"}, "answer": "B"},
        {"id": 77, "question": "Which platform is famous for short vertical videos?", "options": {"A": "TikTok", "B": "LinkedIn", "C": "Reddit", "D": "Pinterest"}, "answer": "A"},
    ],
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
    cats = []
    for name, questions in QUESTIONS.items():
        cats.append({
            "name": name,
            "count": len(questions)
        })
    return jsonify({"categories": cats})


@app.route('/api/quiz/start', methods=['POST'])
def start_quiz():
    data = request.get_json() or {}
    category = data.get("category")
    num = data.get("number_of_questions")

    if not category or num is None:
        return jsonify({"error": "Missing category or number_of_questions"}), 400

    try:
        num = int(num)
    except (TypeError, ValueError):
        return jsonify({"error": "number_of_questions must be a number"}), 400

    cats = {k.lower(): k for k in QUESTIONS}
    if category.lower() not in cats:
        return jsonify({"error": f"Category not found. Available: {list(QUESTIONS.keys())}"}), 404

    official = cats[category.lower()]
    available = list(QUESTIONS[official])

    if num < 1 or num > len(available):
        return jsonify({"error": f"Choose between 1 and {len(available)} questions"}), 400

    random.shuffle(available)
    selected = available[:num]

    quiz_id = str(uuid.uuid4())
    QUIZZES[quiz_id] = {
        "category": official,
        "questions": selected,
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
        "question": q["question"],
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
        "correct_answer": correct,
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
        "completed": quiz["completed"],
        "category": quiz["category"]
    })


if __name__ == '__main__':
    app.run(debug=True)