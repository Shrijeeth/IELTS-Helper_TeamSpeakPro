import streamlit as st
from dotenv import load_dotenv
from st_audiorec import st_audiorec

from backend import generate_questions, utils
from backend import transcribe

load_dotenv()

st.title("IELTS-Helper")

st.subheader("Your Part-1 Test Starts Now")


def question_page(question_text, question_number):
    st.write(f"### Question {question_number}")
    st.write(question_text)
    audio_data = st_audiorec()

    if audio_data is not None:
        st.audio(audio_data, format="audio/wav")
        if st.button("Transcribe", key=f"transcribe_button_{question_number}"):
            response = transcribe.transcribe(audio_data, question_text)
            st.session_state[f"response_{question_number}"] = response
            st.session_state["current_question"] += 1
            st.experimental_rerun()


if "current_question" not in st.session_state:
    st.session_state["current_question"] = 0

if "questions_generated" not in st.session_state:
    st.session_state["questions_generated"] = False

if not st.session_state["questions_generated"]:
    utils.create_file("Answers_part01.txt")
    generate_questions.generate_part1()
    st.session_state["questions_generated"] = True

lines = generate_questions.load_questions("./backend/data/Question_for_part01.txt")

current_question = st.session_state["current_question"]

if current_question < len(lines):
    question = lines[current_question].strip()
    question_page(question, current_question + 1)
else:
    st.write("### All questions have been answered.")
    st.write("Thank you for your responses!")
    for i in range(len(lines)):
        response = st.session_state.get(f"response_{i}", None)
        st.write(f"**Transcription for Question {i + 1}:** {response}")