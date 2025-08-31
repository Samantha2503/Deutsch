import streamlit as st
import pandas as pd
import random
import os

CSV_FILE = "Deutsch/vocab.csv"


def color_article(word: str) -> str:
    if word.startswith("der "):
        return f"<span style='color:blue;font-weight:bold;'>der</span> {word[4:]}"
    elif word.startswith("die "):
        return f"<span style='color:red;font-weight:bold;'>die</span> {word[4:]}"
    elif word.startswith("das "):
        return f"<span style='color:green;font-weight:bold;'>das</span> {word[4:]}"
    return word


# --- Helper functions ---
def load_vocab():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["word", "translation"])
        df.to_csv(CSV_FILE, index=False)
    return pd.read_csv(CSV_FILE)

def save_vocab(df):
    df.to_csv(CSV_FILE, index=False)

def get_word_dict():
    df = load_vocab()
    return dict(zip(df["word"], df["translation"]))

# Load words
WORDS = get_word_dict()

# --- Session state ---
if "index" not in st.session_state:
    st.session_state.index = 0
if "score_typing" not in st.session_state:
    st.session_state.score_typing = 0
if "score_quiz" not in st.session_state:
    st.session_state.score_quiz = 0

# Create shuffled word list for practice
if "word_list" not in st.session_state or not st.session_state.word_list:
    st.session_state.word_list = list(WORDS.items())
    random.shuffle(st.session_state.word_list)

st.title("📚 German Vocabulary Trainer")

tabs = st.tabs(["📖 Flashcards", "⌨️ Typing Practice", "❓ Quiz","Widerholung"])

# --- Tab 1: Flashcards ---
with tabs[0]:
    st.subheader("Flashcards")
    if not WORDS:
        st.warning("No words yet! Add some first.")
    else:
        word, translation = st.session_state.word_list[st.session_state.index]
        st.markdown(f"👉 **{color_article(word)}**", unsafe_allow_html=True)


        if "show_meaning" not in st.session_state:
            st.session_state.show_meaning = False

        if st.button("Show meaning", key="flashcard_show"):
            st.session_state.show_meaning = True

        if st.session_state.show_meaning:
            st.success(translation)

        if st.button("Next word ➡️", key="flashcard_next"):
            st.session_state.index = (st.session_state.index + 1) % len(st.session_state.word_list)
            st.session_state.show_meaning = False
            st.rerun()

# --- Tab 2: Typing Practice ---
with tabs[1]:
    st.subheader("Typing Practice")
    if not WORDS:
        st.warning("No words yet! Add some first.")
    else:
        word, translation = st.session_state.word_list[st.session_state.index]
        st.write(f"👉 What does **{word}** mean?")

        user_answer = st.text_input("Your answer:", key="typing_input")

        if st.button("Check", key="typing_check"):
            if user_answer.lower().strip() == translation.lower():
                st.success("✅ Correct!")
                st.session_state.score_typing += 1
            else:
                st.error(f"❌ Wrong! Correct: {translation}")

        if st.button("Next word ➡️", key="typing_next"):
            st.session_state.index = (st.session_state.index + 1) % len(st.session_state.word_list)
            st.rerun()

    st.info(f"Score: {st.session_state.score_typing}")

# --- Tab 3: Multiple Choice Quiz ---
with tabs[2]:
    st.subheader("Multiple Choice Quiz")
    if not WORDS:
        st.warning("No words yet! Add some first.")
    else:
        word, correct = st.session_state.word_list[st.session_state.index]

        st.write(f"👉 What does **{word}** mean?")

        # Initialize options only for the current word
        if "quiz_options" not in st.session_state or st.session_state.current_word_quiz != word:
            options = list(WORDS.values())
            random.shuffle(options)
            if correct not in options[:3]:
                options = options[:3] + [correct]
            random.shuffle(options)
            st.session_state.quiz_options = options
            st.session_state.current_word_quiz = word

        choice = st.radio("Choose the meaning:", st.session_state.quiz_options, key="quiz_radio")

        if st.button("Submit", key="quiz_submit"):
            if choice == correct:
                st.success("✅ Correct!")
                st.session_state.score_quiz += 1
            else:
                st.error(f"❌ Wrong! It means: {correct}")

        if st.button("Next word ➡️", key="quiz_next"):
            st.session_state.index = (st.session_state.index + 1) % len(st.session_state.word_list)
            # Clear stored options for next word
            st.session_state.pop("quiz_options", None)
            st.session_state.pop("current_word_quiz", None)
            st.rerun()

    st.info(f"Score: {st.session_state.score_quiz}")

# --- Tab 4: Writing Practice ---

with tabs[3]:
    st.subheader("✍️ Writing Practice")
    if not WORDS:
        st.warning("No words yet! Add some first.")
    else:
        word, translation = st.session_state.word_list[st.session_state.index]
        
        st.markdown(f"**Word:** {color_article(word)}", unsafe_allow_html=True)
        st.write(f"**Meaning:** {translation}")

        # Use a form to handle input
        with st.form(key="writing_form"):
            user_input = st.text_input("Write the word here:")
            submitted = st.form_submit_button("Check")

            if submitted:
                if user_input.lower().strip() == word.lower():
                    st.success("✅ Correct!")
                    st.session_state.score_writing = st.session_state.get("score_writing", 0) + 1
                else:
                    st.error(f"❌ Wrong! Correct: {word}")

                # Move to next word
                st.session_state.index = (st.session_state.index + 1) % len(st.session_state.word_list)
                st.experimental_rerun()  # Clears the input field



