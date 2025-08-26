import streamlit as st
import random

# List of verbs with prepositions, case, and Spanish translation
verbs = [
    {"verb": "achten", "prep": "auf", "case": "Akk", "translation": "prestar atención a"},
    {"verb": "sich engagieren", "prep": "für", "case": "Akk", "translation": "comprometerse con"},
    {"verb": "sich entschuldigen", "prep": "bei", "case": "Dat", "translation": "disculparse con"},
    {"verb": "sich entschuldigen", "prep": "für", "case": "Akk", "translation": "disculparse por"},
    {"verb": "reagieren", "prep": "auf", "case": "Akk", "translation": "reaccionar a"},
    {"verb": "anfangen", "prep": "mit", "case": "Dat", "translation": "empezar con"},
    {"verb": "schicken", "prep": "an", "case": "Akk", "translation": "enviar a"},
    {"verb": "antworten", "prep": "auf", "case": "Akk", "translation": "responder a"},
    {"verb": "sprechen", "prep": "über", "case": "Akk", "translation": "hablar sobre"},
    {"verb": "sich ärgern", "prep": "über", "case": "Akk", "translation": "enfadarse por"},
    {"verb": "sich erinnern", "prep": "an", "case": "Akk", "translation": "acordarse de"},
    {"verb": "fragen", "prep": "nach", "case": "Dat", "translation": "preguntar por"},
    {"verb": "aufpassen", "prep": "auf", "case": "Akk", "translation": "cuidar de"},
    {"verb": "sich aufregen", "prep": "über", "case": "Akk", "translation": "alterarse por"},
    {"verb": "sich freuen", "prep": "über", "case": "Akk", "translation": "alegrarse por"},
    {"verb": "teilnehmen", "prep": "an", "case": "Dat", "translation": "participar en"},
    {"verb": "sich bedanken", "prep": "für", "case": "Akk", "translation": "agradecer por"},
    {"verb": "sich bedanken", "prep": "bei", "case": "Dat", "translation": "agradecer a"},
    {"verb": "telefonieren", "prep": "mit", "case": "Dat", "translation": "hablar por teléfono con"},
    {"verb": "gehören", "prep": "zu", "case": "Dat", "translation": "pertenecer a"},
    {"verb": "sich gewöhnen", "prep": "an", "case": "Akk", "translation": "acostumbrarse a"},
    {"verb": "sich treffen", "prep": "mit", "case": "Dat", "translation": "encontrarse con"},
    {"verb": "beginnen", "prep": "mit", "case": "Dat", "translation": "comenzar con"},
    {"verb": "träumen", "prep": "von", "case": "Dat", "translation": "soñar con"},
    {"verb": "sich beschweren", "prep": "über", "case": "Akk", "translation": "quejarse de"},
    {"verb": "sich beschweren", "prep": "bei", "case": "Dat", "translation": "quejarse ante"},
    {"verb": "glauben", "prep": "an", "case": "Akk", "translation": "creer en"},
    {"verb": "sich unterhalten", "prep": "über", "case": "Akk", "translation": "conversar sobre"},
    {"verb": "gratulieren", "prep": "zu", "case": "Dat", "translation": "felicitar por"},
    {"verb": "sich bewerben", "prep": "um", "case": "Akk", "translation": "postularse a"},
    {"verb": "sich bewerben", "prep": "bei", "case": "Dat", "translation": "postularse en"},
    {"verb": "hoffen", "prep": "auf", "case": "Akk", "translation": "esperar (algo)"},
    {"verb": "sich verlassen", "prep": "auf", "case": "Akk", "translation": "confiar en"},
    {"verb": "bitten", "prep": "um", "case": "Akk", "translation": "pedir algo"},
    {"verb": "sich informieren", "prep": "über", "case": "Akk", "translation": "informarse sobre"},
    {"verb": "sich informieren", "prep": "bei", "case": "Dat", "translation": "informarse con"},
    {"verb": "verzichten", "prep": "auf", "case": "Akk", "translation": "renunciar a"},
    {"verb": "danken", "prep": "für", "case": "Akk", "translation": "agradecer por"},
    {"verb": "denken", "prep": "an", "case": "Akk", "translation": "pensar en"},
    {"verb": "sich interessieren", "prep": "für", "case": "Akk", "translation": "interesarse por"},
    {"verb": "sich vorbereiten", "prep": "auf", "case": "Akk", "translation": "prepararse para"},
    {"verb": "diskutieren", "prep": "über", "case": "Akk", "translation": "debatir sobre"},
    {"verb": "diskutieren", "prep": "mit", "case": "Dat", "translation": "debatir con"},
    {"verb": "sich kümmern", "prep": "um", "case": "Akk", "translation": "ocuparse de"},
    {"verb": "warten", "prep": "auf", "case": "Akk", "translation": "esperar a"},
    {"verb": "einladen", "prep": "zu", "case": "Dat", "translation": "invitar a"},
    {"verb": "lachen", "prep": "über", "case": "Akk", "translation": "reírse de"},
    {"verb": "nachdenken", "prep": "über", "case": "Akk", "translation": "reflexionar sobre"},
    {"verb": "sich wundern", "prep": "über", "case": "Akk", "translation": "sorprenderse de"},
    {"verb": "zweifeln", "prep": "an", "case": "Dat", "translation": "dudar de"}
]

# ----------------------------
# SESSION STATE INIT
# ----------------------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = []
if "current_q" not in st.session_state:
    st.session_state.current_q = random.choice(verbs)
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "prep" not in st.session_state:
    st.session_state.prep = ""
if "case" not in st.session_state:
    st.session_state.case = "Akk"
if "flashcard_index" not in st.session_state:
    st.session_state.flashcard_index = random.randint(0, len(verbs)-1)
if "show_translation" not in st.session_state:
    st.session_state.show_translation = False

# ----------------------------
# TABS
# ----------------------------
tab1, tab2 = st.tabs(["Quiz", "Flashcards"])

# ----------------------------
# QUIZ TAB
# ----------------------------
with tab1:
    st.title("German Verb + Preposition Quiz")
    st.write("Fill in the correct preposition and select the correct case (Akkusativ/Dativ).")

    st.subheader(f"Verb: {st.session_state.current_q['verb']}")

    # Input fields
    st.session_state.prep = st.text_input("Preposition:", value=st.session_state.prep, key="prep_input")
    st.session_state.case = st.radio("Case:", ["Akk", "Dat"], index=0 if st.session_state.case=="Akk" else 1, key="case_radio")

    # Buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Submit") and not st.session_state.submitted:
            st.session_state.submitted = True
            correct_prep = st.session_state.current_q["prep"]
            correct_case = st.session_state.current_q["case"]

            if st.session_state.prep.strip().lower() == correct_prep and st.session_state.case == correct_case:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong. Correct: {correct_prep} ({correct_case})")
                st.session_state.wrong_answers.append(
                    f"{st.session_state.current_q['verb']} {correct_prep} ({correct_case}) → {st.session_state.current_q['translation']}"
                )
            st.info(f"Translation: {st.session_state.current_q['translation']}")

    with col2:
        if st.button("Next Question"):
            st.session_state.current_q = random.choice(verbs)
            st.session_state.submitted = False
            st.session_state.prep = ""
            st.session_state.case = "Akk"

    st.write(f"Score: {st.session_state.score}")
    if st.session_state.wrong_answers:
        with st.expander("Review wrong answers"):
            for item in st.session_state.wrong_answers:
                st.write(item)

# ----------------------------
# FLASHCARD TAB
# ----------------------------
with tab2:
    st.title("Flashcards: German Verb + Preposition")

    card = verbs[st.session_state.flashcard_index]
    st.subheader(f"{card['verb']} {card['prep']} ({card['case']})")

    if st.session_state.show_translation:
        st.info(f"Translation: {card['translation']}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Flip Card"):
            st.session_state.show_translation = not st.session_state.show_translation

    with col2:
        if st.button("Next Card"):
            st.session_state.flashcard_index = random.randint(0, len(verbs)-1)
            st.session_state.show_translation = False
