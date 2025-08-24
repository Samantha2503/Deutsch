import random

# List of verbs with required case and sentence template
verbs = [
    {"verb": "sich freuen", "case": "Akk", "sentence": "{} ___ auf das Wochenende."},
    {"verb": "sich erinnern", "case": "Akk", "sentence": "{} ___ an deinen Geburtstag."},
    {"verb": "sich die Haare kämmen", "case": "Dat", "sentence": "{} ___ die Haare."},
    {"verb": "sich die Hände waschen", "case": "Dat", "sentence": "{} ___ die Hände."},
    {"verb": "sich vorstellen", "case": "Dat", "sentence": "{} ___ einen schönen Urlaub."}
]

# Reflexive pronouns by person
pronouns_akk = {"ich": "mich", "du": "dich", "er": "sich", "sie": "sich", "es": "sich", "wir": "uns", "ihr": "euch", "Sie": "sich"}
pronouns_dat = {"ich": "mir", "du": "dir", "er": "sich", "sie": "sich", "es": "sich", "wir": "uns", "ihr": "euch", "Sie": "sich"}

# Subjects to match pronouns
subjects = {"ich": "Ich", "du": "Du", "er": "Er", "sie": "Sie", "es": "Es", "wir": "Wir", "ihr": "Ihr", "Sie": "Sie"}

print("German Reflexive Pronoun Practice! Type the correct reflexive pronoun.\n")

for _ in range(5):
    q = random.choice(verbs)
    person = random.choice(list(subjects.keys()))
    
    sentence = q["sentence"].format(subjects[person])
    print(f"Sentence: {sentence}")
    
    answer = input("Your answer: ").strip()
    
    correct = pronouns_akk if q["case"] == "Akk" else pronouns_dat
    if answer == correct[person]:
        print("✅ Correct!\n")
    else:
        print(f"❌ Wrong. Correct answer: {correct[person]}\n")
