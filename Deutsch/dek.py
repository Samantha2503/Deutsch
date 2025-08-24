import random

# Adjective endings reference
endings = {
    "definite": {
        "nom": {"m": "e", "f": "e", "n": "e", "pl": "en"},
        "akk": {"m": "en", "f": "e", "n": "e", "pl": "en"},
        "dat": {"m": "en", "f": "en", "n": "en", "pl": "en"}
    },
    "indefinite": {
        "nom": {"m": "er", "f": "e", "n": "es", "pl": "en"},
        "akk": {"m": "en", "f": "e", "n": "es", "pl": "en"},
        "dat": {"m": "en", "f": "en", "n": "en", "pl": "en"}
    },
    "no_article": {
        "nom": {"m": "er", "f": "e", "n": "es", "pl": "e"},
        "akk": {"m": "en", "f": "e", "n": "es", "pl": "e"},
        "dat": {"m": "em", "f": "er", "n": "em", "pl": "en"}
    }
}

# Nouns with gender
nouns = [
    {"noun": "Hund", "gender": "m"}, {"noun": "Katze", "gender": "f"}, {"noun": "Kind", "gender": "n"},
    {"noun": "Bücher", "gender": "pl"}, {"noun": "Auto", "gender": "n"}, {"noun": "Blume", "gender": "f"},
    {"noun": "Mann", "gender": "m"}, {"noun": "Frauen", "gender": "pl"}, {"noun": "Stuhl", "gender": "m"},
    {"noun": "Lampe", "gender": "f"}
]

# Adjectives
adjectives = ["schön", "groß", "klein", "alt", "neu", "interessant", "teuer", "billig", "langsam", "schnell"]

# Articles
articles = {
    "definite": {"m": "der", "f": "die", "n": "das", "pl": "die"},
    "indefinite": {"m": "ein", "f": "eine", "n": "ein", "pl": ""},
    "no_article": {"m": "", "f": "", "n": "", "pl": ""}
}

# Cases
cases = ["nom", "akk", "dat"]

# Track score and wrong answers
score = 0
wrong_answers = []

print("German Adjective Ending Quiz!\nFill in the correct ending for the adjective.\n")

for _ in range(20):  # Number of questions
    noun_info = random.choice(nouns)
    adj = random.choice(adjectives)
    case = random.choice(cases)
    article_type = random.choice(list(articles.keys()))
    
    article = articles[article_type][noun_info["gender"]]
    correct_ending = endings[article_type][case][noun_info["gender"]]
    
    print(f"Case: {case.capitalize()}, Article type: {article_type.capitalize()}")
    print(f"{article} {adj}___ {noun_info['noun']}")
    
    answer = input("Your ending: ").strip()
    
    if answer == correct_ending:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong. Correct ending: {correct_ending}\n")
        wrong_answers.append(f"{article} {adj}___ {noun_info['noun']} (Correct: {correct_ending})")

print(f"Your score: {score}/20\n")

if wrong_answers:
    print("Review the ones you missed:")
    for item in wrong_answers:
        print(item)
