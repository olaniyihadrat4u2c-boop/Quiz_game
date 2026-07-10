import random

#Questions database
QUESTIONS = {
    "General Knowledge": [
        {
            "question": "What is the capital of France?",
            "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
            "answer": "C"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": {"A": "Vincent van Gogh", "B": "Pablo Picasso", "C": "Leonardo da Vinci", "D": "Michelangelo"},
            "answer": "C"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": {"A": "Atlantic Ocean", "B": "Indian Ocean", "C": "Arctic Ocean", "D": "Pacific Ocean"},
            "answer": "D"
        },
        {
            "question": "In which year did the first moon landing occur?",
            "options": {"A": "1965", "B": "1969", "C": "1972", "D": "1963"},
            "answer": "B"
        },
        {
            "question": "What is the currency of Japan?",
            "options": {"A": "Yuan", "B": "Won", "C": "Yen", "D": "Ringgit"},
            "answer": "C"
        },
        {
            "question": "What is the tallest mountain in the world?",
            "options": {"A": "K2", "B": "Kangchenjunga", "C": "Mount Everest", "D": "Lhotse"},
            "answer": "C"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": {"A": "Charles Dickens", "B": "William Shakespeare", "C": "Jane Austen", "D": "Mark Twain"},
            "answer": "B"
        },
        {
            "question": "What is the capital of Australia?",
            "options": {"A": "Sydney", "B": "Melbourne", "C": "Canberra", "D": "Brisbane"},
            "answer": "C"
        },
        {
            "question": "In which country is the Great Wall located?",
            "options": {"A": "Japan", "B": "India", "C": "China", "D": "Russia"},
            "answer": "C"
        },
        {
            "question": "What is the largest continent?",
            "options": {"A": "Africa", "B": "Asia", "C": "North America", "D": "Europe"},
            "answer": "B"
        },
        {
            "question": "Who was the first President of the United States?",
            "options": {"A": "Thomas Jefferson", "B": "Abraham Lincoln", "C": "George Washington", "D": "John Adams"},
            "answer": "C"
        },
        {
            "question": "What is the smallest country in the world?",
            "options": {"A": "Monaco", "B": "Vatican City", "C": "San Marino", "D": "Liechtenstein"},
            "answer": "B"
        }
    ],
    "Science": [
        {
            "question": "What is the closest planet to the Sun?",
            "options": {"A": "Earth", "B": "Venus", "C": "Mars", "D": "Mercury"},
            "answer": "D"
        },
        {
            "question": "How many bones are in the adult human body?",
            "options": {"A": "206", "B": "312", "C": "175", "D": "250"},
            "answer": "A"
        },
        {
            "question": "What gas do plants absorb from the air?",
            "options": {"A": "Oxygen", "B": "Nitrogen", "C": "Carbon Dioxide", "D": "Hydrogen"},
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for Gold?",
            "options": {"A": "Go", "B": "Gd", "C": "Au", "D": "Ag"},
            "answer": "C"
        },
        {
            "question": "What is the powerhouse of the cell?",
            "options": {"A": "Nucleus", "B": "Mitochondria", "C": "Ribosome", "D": "Endoplasmic Reticulum"},
            "answer": "B"
        },
        {
            "question": "What is the speed of light in vacuum?",
            "options": {"A": "299,792 km/s", "B": "150,000 km/s", "C": "500,000 km/s", "D": "1,000,000 km/s"},
            "answer": "A"
        },
        {
            "question": "What is H2O commonly known as?",
            "options": {"A": "Salt", "B": "Water", "C": "Sugar", "D": "Oxygen"},
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": {"A": "Venus", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
            "answer": "B"
        },
        {
            "question": "What organ pumps blood in the human body?",
            "options": {"A": "Liver", "B": "Kidney", "C": "Heart", "D": "Lung"},
            "answer": "C"
        },
        {
            "question": "What is the atomic number of Carbon?",
            "options": {"A": "6", "B": "8", "C": "12", "D": "14"},
            "answer": "A"
        },
        {
            "question": "What force keeps planets in orbit?",
            "options": {"A": "Magnetism", "B": "Gravity", "C": "Friction", "D": "Electricity"},
            "answer": "B"
        },
        {
            "question": "What is the main gas in Earth's atmosphere?",
            "options": {"A": "Oxygen", "B": "Carbon Dioxide", "C": "Nitrogen", "D": "Hydrogen"},
            "answer": "C"
        }
    ],
    "Anime & Manga": [
        {
            "question": "Who is the main character in Naruto?",
            "options": {"A": "Sasuke Uchiha", "B": "Naruto Uzumaki", "C": "Kakashi Hatake", "D": "Sakura Haruno"},
            "answer": "B"
        },
        {
            "question": "What is the name of the sword used by Ichigo in Bleach?",
            "options": {"A": "Zangetsu", "B": "Bankai", "C": "Excalibur", "D": "Muramasa"},
            "answer": "A"
        },
        {
            "question": "In One Piece, what is the name of Luffy's ship?",
            "options": {"A": "Going Merry", "B": "Thousand Sunny", "C": "Moby Dick", "D": "Black Pearl"},
            "answer": "B"
        },
        {
            "question": "Who created Dragon Ball?",
            "options": {"A": "Eiichiro Oda", "B": "Masashi Kishimoto", "C": "Akira Toriyama", "D": "Tite Kubo"},
            "answer": "C"
        },
        {
            "question": "What anime features a character named Light Yagami?",
            "options": {"A": "Death Note", "B": "Attack on Titan", "C": "Fullmetal Alchemist", "D": "Hunter x Hunter"},
            "answer": "A"
        },
        {
            "question": "What is Goku's signature attack?",
            "options": {"A": "Rasengan", "B": "Kamehameha", "C": "Bankai", "D": "Susanoo"},
            "answer": "B"
        },
        {
            "question": "In Attack on Titan, what are the giant creatures called?",
            "options": {"A": "Hollows", "B": "Titans", "C": "Akuma", "D": "Youma"},
            "answer": "B"
        },
        {
            "question": "Who is the author of One Piece?",
            "options": {"A": "Akira Toriyama", "B": "Eiichiro Oda", "C": "Masashi Kishimoto", "D": "Yoshihiro Togashi"},
            "answer": "B"
        },
        {
            "question": "What is the name of the protagonist in Death Note?",
            "options": {"A": "L", "B": "Light Yagami", "C": "Misa Amane", "D": "Near"},
            "answer": "B"
        },
        {
            "question": "Which anime has a character named Edward Elric?",
            "options": {"A": "Naruto", "B": "Fullmetal Alchemist", "C": "Bleach", "D": "One Piece"},
            "answer": "B"
        },
        {
            "question": "What is the main power system in Hunter x Hunter?",
            "options": {"A": "Chakra", "B": "Nen", "C": "Reiatsu", "D": "Haki"},
            "answer": "B"
        },
        {
            "question": "Who is the captain of the Straw Hat Pirates?",
            "options": {"A": "Zoro", "B": "Sanji", "C": "Luffy", "D": "Nami"},
            "answer": "C"
        }
    ]
}

CATEGORIES = list(QUESTIONS.keys())

def access_engine():
    """Welcomes the user and lets them pick a quiz category and number of questions."""
    print("=" * 30)
    print("Welcome to QuizGame!")
    print("=" * 30)
    print("\nRules:")
    print("- Answer with A, B, C, or D")
    print("- You have 3 strikes (wrong answers)")
    print("- 3 strikes ends the game early")
    print("- Choose a category and number of questions below\n")
    
    while True:
        print("Available Categories:")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"{i}. {cat}")
        
        try:
            choice = int(input("\nEnter the number of your chosen category: "))
            if 1 <= choice <= len(CATEGORIES):
                selected = CATEGORIES[choice - 1]
                print(f"\nYou chose: {selected}")
                
                # Ask for number of questions
                max_q = len(QUESTIONS[selected])
                while True:
                    try:
                        num_questions = int(input(f"How many questions do you want to answer? (1-{max_q}): "))
                        if 1 <= num_questions <= max_q:
                            print(f"Get ready! The quiz will begin now with {num_questions} questions.")
                            print("You have 3 strikes. 3 wrong answers and the game ends early.")
                            return selected, num_questions
                        else:
                            print(f"Invalid number. Please enter between 1 and {max_q}.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(CATEGORIES)}")
        except ValueError:
            print("Invalid input. Please enter a number.")

def question_loader(category, num_questions=None):
    #this recievies the category and returns the right questions for that categorie
    if category in QUESTIONS:
        #randomize order, no repeats
        questions = QUESTIONS[category][:]
        random.shuffle(questions)
        if num_questions and num_questions < len(questions):
            return questions[:num_questions]
        return questions
    return []

def quiz_engine(questions):
    """Runs the quiz loop. Returns score and total questions attempted."""
    score = 0
    strikes = 3
    total = len(questions)
    answered = 0
    
    print("-" * 30)
    
    for i, q in enumerate(questions, 1):
        if strikes <= 0:
            break
        
        print(f"\nQuestion {i} of {total}:")
        print(q["question"])
        for opt, ans in q["options"].items():
            print(f"{opt}) {ans}")
        
        while True:
            user_input = input("\nYour answer (A/B/C/D): ").strip().upper()
            if user_input in ['A', 'B', 'C', 'D']:
                answered += 1
                if user_input == q["answer"]:
                    print("Correct! ✓")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was {q['answer']}) {q['options'][q['answer']]} ✗")
                    strikes -= 1
                print(f"Strikes remaining: {strikes}")
                break
            else:
                print("Invalid input. Only A, B, C or D are accepted.")
                print("This counts as a wrong answer!")
                strikes -= 1
                print(f"Strikes remaining: {strikes}")
                answered += 1  # Counts as attempted
                break
        
        if strikes <= 0:
            print("\nYou've used all 3 strikes. Game over!")
            break
    
    return score, answered if answered > 0 else total

def result_engine(score, total):
    """Displays the final result."""
    if total == 0:
        print("No questions were answered.")
        return
    
    percentage = (score / total) * 100
    print("\n" + "=" * 30)
    print("QUIZ COMPLETE!")
    print("=" * 30)
    print(f"Your Score: {score} out of {total}")
    print(f"Percentage: {int(percentage)}%")
    
    if percentage >= 90:
        grade = "A"
        msg = "Outstanding! Perfect knowledge!"
    elif percentage >= 75:
        grade = "B"
        msg = "Great job! Really solid!"
    elif percentage >= 55:
        grade = "C"
        msg = "Not bad! A bit more study will help."
    elif percentage >= 40:
        grade = "D"
        msg = "You passed, but there's room to improve."
    else:
        grade = "F"
        msg = "Keep practicing, you'll get there!"
    
    print(f"Grade: {grade} — {msg}")