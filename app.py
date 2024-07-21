import streamlit as st
from dotenv import load_dotenv
from st_audiorec import st_audiorec

from backend import generate_questions, utils, evaluate_answers
from backend import transcribe

load_dotenv()

st.title("SpeakPro")

parts = ["Part 1", "Part 2", "Part 3"]

if "current_part" not in st.session_state:
    st.session_state["current_part"] = 0

if "answers_generated" not in st.session_state:
    st.session_state["answers_generated"] = False

for part in parts:
    if f"current_question_{part}" not in st.session_state:
        st.session_state[f"current_question_{part}"] = 0

    if f"questions_generated_{part}" not in st.session_state:
        st.session_state[f"questions_generated_{part}"] = False


def question_page(question_text, question_number, part_str):
    st.write(f"### {part_str} - Question {question_number}")
    st.write(question_text)
    audio_data = st_audiorec()

    if audio_data is not None:
        if st.button("Submit", key=f"transcribe_button_{part}_{question_number}"):
            response = transcribe.transcribe(audio_data, question_text)
            st.session_state[f"response_{part_str}_{question_number}"] = response
            st.session_state[f"current_question_{part_str}"] += 1
            st.experimental_rerun()


def load_questions_for_part(part_str):
    if not st.session_state[f"answers_generated"]:
        utils.create_file(f"Answers.txt")
        st.session_state[f"answers_generated"] = True
    if not st.session_state[f"questions_generated_{part_str}"]:
        generate_questions.generate_part(part_str)
        st.session_state[f"questions_generated_{part_str}"] = True
    return generate_questions.load_questions(f"./backend/data/Question_for_{part_str.replace(' ', '')}.txt")


current_part = parts[st.session_state["current_part"]]
lines = load_questions_for_part(current_part)

current_question = st.session_state[f"current_question_{current_part}"]

if current_question < len(lines):
    question = lines[current_question].strip()
    question_page(question, current_question + 1, current_part)
else:
    st.write(f"### All questions have been answered in {current_part}.")
    st.session_state["current_part"] += 1
    if st.session_state["current_part"] < len(parts):
        st.experimental_rerun()
    else:
        st.write("### All parts have been completed. Thank you for your responses!")
        st.write("### Here is your detailed AI Feedback:")
        st.write(evaluate_answers.request_feedback())
