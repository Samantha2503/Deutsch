import random

# List of verbs with their case and English translation
verbs = [
    {"verb": "sich freuen", "case": "Akk", "english": "to look forward to / be happy"},
    {"verb": "sich erinnern", "case": "Akk", "english": "to remember"},
    {"verb": "sich verlieben", "case": "Akk", "english": "to fall in love"},
    {"verb": "sich die Haare kämmen", "case": "Dat", "english": "to comb one’s hair"},
    {"verb": "sich die Hände waschen", "case": "Dat", "english": "to wash one’s hands"},
    {"verb": "sich etwas vorstellen", "case": "Dat", "english": "to imagine something"},
    {"verb": "sich etwas leisten", "case": "Dat", "english": "to afford something"},
    {"verb": "sich fühlen", "case": "Akk", "english": "to feel (emotion)"},
    {"verb": "sich sehen", "case": "Akk", "english": "to see oneself"},
]

print("German Reflexive Verb Quiz! Type 'Akk' for Akkusativ or 'Dat' for Dativ.\n")

score = 0

for _ in range(10):
    q = random.choice(verbs)
    print(f"Verb: {q['verb']} ({q['english']})")
    answer = input("Case (Akk/Dat): ").strip().capitalize()
    
    if answer == q["case"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong. Correct answer: {q['case']}\n")

print(f"Your score: {score}/10")
