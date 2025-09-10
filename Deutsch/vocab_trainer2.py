import streamlit as st
import pandas as pd
import random
import os

CSV_FILE = "Deutsch/word.csv"

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
        df = pd.DataFrame(columns=["word", "translation", "lektion"])
        df.to_csv(CSV_FILE, index=False)
    return pd.read_csv(CSV_FILE)

def save_vocab(df):
    df.to_csv(CSV_FILE, index=False)

def get_word_dict(df):
    """Return word→translation dictionary (ignores lektion)."""
    return dict(zip(df["word"], df["translation"]))

# --- Load words ---
df = load_vocab()
WORDS = get_word_dict(df)

# --- Session state ---
if "index" not in st.session_state:
    st.session_state.index = 0
if "score_typing" not in st.session_state:
    st.session_state.score_typing = 0
if "score_quiz" not in st.session_state:
    st.session_state.score_quiz = 0

# Make sure 'lektion' column exists
if "lektion" not in df.columns:
    df["lektion"] = 0  # default if missing

# Let user choose which set to review
set_ids = sorted(df["lektion"].unique())
chosen_set = st.selectbox("Choose set to review:", set_ids)

# Filter word list by chosen lektion
filtered_words = df[df["lektion"] == chosen_set][["word", "translation"]].values.tolist()

# --- Session state initialization ---
if "show_meaning" not in st.session_state:
    st.session_state.show_meaning = False
if "word_list" not in st.session_state or filtered_words != st.session_state.word_list:
    st.session_state.word_list = filtered_words
    st.session_state.index = 0
    st.session_state.show_meaning = False

st.title("📚 German Vocabulary Trainer")

tabs = st.tabs(["📖 Flashcards", "⌨️ Typing Practice", "❓ Quiz", "✍️ Writing"])

# --- Tab 1: Flashcards ---
with tabs[0]:
    st.subheader("Flashcards")

    if not st.session_state.word_list:
        st.warning("No words available for this set.")
    else:
        word, translation = st.session_state.word_list[st.session_state.index]
        st.markdown(f"👉 **{color_article(word)}**", unsafe_allow_html=True)

        if st.button("Show meaning"):
            st.session_state.show_meaning = True

        if st.session_state.show_meaning:
            st.success(translation)

        if st.button("Next word ➡️"):
            st.session_state.index = (st.session_state.index + 1) % len(st.session_state.word_list)
            st.session_state.show_meaning = False
            st.rerun()

# --- Tab 2: Typing Practice ---
with tabs[1]:
    st.subheader("Typing Practice")
    if not st.session_state.word_list:
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
    if not st.session_state.word_list:
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
    if not st.session_state.word_list:
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
                st.experimental_user()  # Clears the input field
