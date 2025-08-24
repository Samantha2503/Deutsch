import random

# List of 100 nouns with their articles
nouns = [
    ("Apfel", "der"), ("Banane", "die"), ("Buch", "das"), ("Tisch", "der"), ("Lampe", "die"),
    ("Auto", "das"), ("Stuhl", "der"), ("Blume", "die"), ("Haus", "das"), ("Hund", "der"),
    ("Katze", "die"), ("Fenster", "das"), ("Baum", "der"), ("Tür", "die"), ("Kind", "das"),
    ("Stift", "der"), ("Uhr", "die"), ("Mädchen", "das"), ("Schrank", "der"), ("Straße", "die"),
    ("Bett", "das"), ("Sessel", "der"), ("Flasche", "die"), ("Bild", "das"), ("Schreibtisch", "der"),
    ("Wand", "die"), ("Spielzeug", "das"), ("Schuh", "der"), ("Tasche", "die"), ("Kleid", "das"),
    ("Computer", "der"), ("Brille", "die"), ("Telefon", "das"), ("Bleistift", "der"), ("Zeitung", "die"),
    ("Hausaufgabe", "die"), ("Heft", "das"), ("Papier", "das"), ("Kühlschrank", "der"), ("Schokolade", "die"),
    ("Radio", "das"), ("Brot", "das"), ("Fisch", "der"), ("Kamera", "die"), ("Spiel", "das"),
    ("Löffel", "der"), ("Gabel", "die"), ("Messer", "das"), ("Schule", "die"), ("Lehrer", "der"),
    ("Schülerin", "die"), ("Buchhandlung", "die"), ("Restaurant", "das"), ("Bahnhof", "der"), ("Torte", "die"),
    ("Fahrrad", "das"), ("Zug", "der"), ("U-Bahn", "die"), ("Flugzeug", "das"), ("Berg", "der"),
    ("Insel", "die"), ("Meer", "das"), ("See", "der"), ("Blatt", "das"), ("Blume", "die"),
    ("Apotheke", "die"), ("Krankenhaus", "das"), ("Polizist", "der"), ("Ärztin", "die"), ("Kindergarten", "der"),
    ("Universität", "die"), ("Museum", "das"), ("Park", "der"), ("Brücke", "die"), ("Theater", "das"),
    ("Film", "der"), ("Serie", "die"), ("Kino", "das"), ("Markt", "der"), ("Supermarkt", "der"),
    ("Bäckerei", "die"), ("Metzgerei", "die"), ("Café", "das"), ("Restaurant", "das"), ("Bahnhof", "der"),
    ("Taxi", "das"), ("Bus", "der"), ("Fahrrad", "das"), ("Auto", "das"), ("Motorrad", "das"),
    ("Laden", "der"), ("Shop", "der"), ("Kiosk", "der"), ("Apfel", "der"), ("Birne", "die"),
    ("Traube", "die"), ("Pfirsich", "der"), ("Erdbeere", "die"), ("Himbeere", "die"), ("Zitrone", "die"),
    ("Kirsche", "die"), ("Melone", "die"), ("Ananas", "die"), ("Pflaume", "die"), ("Mango", "die")
]

score = 0
print("German Gender Quiz! Type 'der', 'die', or 'das' for each noun.\n")

for _ in range(10):  # quiz length
    noun, correct_article = random.choice(nouns)
    answer = input(f"Article for '{noun}': ").strip().lower()
    
    if answer == correct_article:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong. Correct answer: {correct_article}\n")

print(f"Your score: {score}/10")
