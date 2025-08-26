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






verbs2 = [
    {"verb": "achten", "prep": "auf", "case": "Akk", "translation": "prestar atención a"},
    {"verb": "antworten", "prep": "auf", "case": "Akk", "translation": "responder a"},
    {"verb": "sich freuen", "prep": "auf", "case": "Akk", "translation": "esperar con ilusión"},
    {"verb": "warten", "prep": "auf", "case": "Akk", "translation": "esperar a"},
    {"verb": "sich konzentrieren", "prep": "auf", "case": "Akk", "translation": "concentrarse en"},
    {"verb": "sich vorbereiten", "prep": "auf", "case": "Akk", "translation": "prepararse para"},
    {"verb": "sich verlassen", "prep": "auf", "case": "Akk", "translation": "confiar en"},
    {"verb": "sich beziehen", "prep": "auf", "case": "Akk", "translation": "referirse a"},
    {"verb": "hoffen", "prep": "auf", "case": "Akk", "translation": "esperar (algo)"},
    {"verb": "sich ärgern", "prep": "über", "case": "Akk", "translation": "enfadarse por"},
    {"verb": "sprechen", "prep": "über", "case": "Akk", "translation": "hablar sobre"},
    {"verb": "sich informieren", "prep": "über", "case": "Akk", "translation": "informarse sobre"},
    {"verb": "diskutieren", "prep": "über", "case": "Akk", "translation": "discutir sobre"},
    {"verb": "sich kümmern", "prep": "um", "case": "Akk", "translation": "ocuparse de"},
    {"verb": "bitten", "prep": "um", "case": "Akk", "translation": "pedir / rogar por"},
    {"verb": "sich sorgen", "prep": "um", "case": "Akk", "translation": "preocuparse por"},
    {"verb": "glauben", "prep": "an", "case": "Akk", "translation": "creer en"},
    {"verb": "denken", "prep": "an", "case": "Akk", "translation": "pensar en"},
    {"verb": "sich erinnern", "prep": "an", "case": "Akk", "translation": "recordar algo"},
    {"verb": "teilnehmen", "prep": "an", "case": "Dat", "translation": "participar en"},
    {"verb": "arbeiten", "prep": "an", "case": "Dat", "translation": "trabajar en"},
    {"verb": "leiden", "prep": "an", "case": "Dat", "translation": "sufrir de"},
    {"verb": "helfen", "prep": "bei", "case": "Dat", "translation": "ayudar en"},
    {"verb": "sich bedanken", "prep": "bei", "case": "Dat", "translation": "agradecer a"},
    {"verb": "sich entschuldigen", "prep": "bei", "case": "Dat", "translation": "disculparse con"},
    {"verb": "sich erkundigen", "prep": "bei", "case": "Dat", "translation": "informarse con"},
    {"verb": "fragen", "prep": "nach", "case": "Dat", "translation": "preguntar por"},
    {"verb": "suchen", "prep": "nach", "case": "Dat", "translation": "buscar"},
    {"verb": "sich sehnen", "prep": "nach", "case": "Dat", "translation": "añorar"},
    {"verb": "zufrieden sein", "prep": "mit", "case": "Dat", "translation": "estar satisfecho con"},
    {"verb": "sich treffen", "prep": "mit", "case": "Dat", "translation": "encontrarse con"},
    {"verb": "sprechen", "prep": "mit", "case": "Dat", "translation": "hablar con"},
    {"verb": "telefonieren", "prep": "mit", "case": "Dat", "translation": "telefonear con"},
    {"verb": "anfangen", "prep": "mit", "case": "Dat", "translation": "empezar con"},
    {"verb": "aufhören", "prep": "mit", "case": "Dat", "translation": "terminar con"},
    {"verb": "rechnen", "prep": "mit", "case": "Dat", "translation": "contar con"},
    {"verb": "zusammenarbeiten", "prep": "mit", "case": "Dat", "translation": "colaborar con"},
    {"verb": "einverstanden sein", "prep": "mit", "case": "Dat", "translation": "estar de acuerdo con"},
    {"verb": "sich gewöhnen", "prep": "an", "case": "Akk", "translation": "acostumbrarse a"},
    {"verb": "interessiert sein", "prep": "an", "case": "Dat", "translation": "estar interesado en"},
    {"verb": "sich beschäftigen", "prep": "mit", "case": "Dat", "translation": "ocuparse de"},
    {"verb": "sich verlieben", "prep": "in", "case": "Akk", "translation": "enamorarse de"},
    {"verb": "sich freuen", "prep": "über", "case": "Akk", "translation": "alegrarse por"},
    {"verb": "berichten", "prep": "über", "case": "Akk", "translation": "informar sobre"},
    {"verb": "sich wundern", "prep": "über", "case": "Akk", "translation": "sorprenderse por"},
    {"verb": "sich beklagen", "prep": "über", "case": "Akk", "translation": "quejarse de"},
    {"verb": "sich streiten", "prep": "über", "case": "Akk", "translation": "discutir sobre"},
    {"verb": "denken", "prep": "über", "case": "Akk", "translation": "reflexionar sobre"},
    {"verb": "sich informieren", "prep": "über", "case": "Akk", "translation": "informarse sobre"}
]


# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = []
if "current_q" not in st.session_state:
    st.session_state.current_q = random.choice(verbs)
if "submitted" not in st.session_state:
    st.session_state.submitted = False

st.title("German Verb + Preposition Quiz")
st.write("Fill in the correct preposition and select the correct case (Akkusativ/Dativ).")

# Display current question
st.subheader(f"Verb: {st.session_state.current_q['verb']}")

prep_answer = st.text_input("Preposition:", key="prep")
case_answer = st.radio("Case:", ["Akk", "Dat"], key="case")

if st.button("Submit") and not st.session_state.submitted:
    st.session_state.submitted = True
    
    correct_prep = st.session_state.current_q["prep"]
    correct_case = st.session_state.current_q["case"]
    
    if prep_answer.strip().lower() == correct_prep and case_answer == correct_case:
        st.success("✅ Correct!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Wrong. Correct: {correct_prep} ({correct_case})")
        st.session_state.wrong_answers.append(
            f"{st.session_state.current_q['verb']} {correct_prep} ({correct_case}) → {st.session_state.current_q['translation']}"
        )
    st.info(f"Translation: {st.session_state.current_q['translation']}")

# if "current_q" not in st.session_state:
#      st.session_state.current_q = random.choice(verbs)
#if "submitted" not in st.session_state: 
#      st.session_state.submitted = False
    
if st.button("Next Question"):
    st.session_state.current_q = random.choice(verbs)
    st.session_state.submitted = False
    #st.stop()






    

st.write(f"Score: {st.session_state.score}")
if st.session_state.wrong_answers:
    with st.expander("Review wrong answers"):
        for item in st.session_state.wrong_answers:
            st.write(item)
