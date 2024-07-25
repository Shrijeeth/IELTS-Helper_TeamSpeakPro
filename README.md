# SpeakPro - IELTS Speaking Module Helper


## Description

SpeakPro is an innovative AI-based tool designed to help students prepare for the IELTS speaking module. Our mission is to provide personalized, real-time feedback to enhance the speaking skills of users, making them more confident and proficient for their exams. SpeakPro conducts mock speaking interviews, evaluates performance, and highlights both strengths and weaknesses within minutes.

## Features

- AI-Powered Mock Interviews: Engage in realistic speaking simulations powered by advanced AI to mirror the actual IELTS speaking test experience.
- Personalized Feedback: Receive detailed, individualized feedback on your performance, pinpointing specific areas for improvement.
- Strengths and Weaknesses Analysis: Understand your strengths and areas that need work to better focus your study efforts.
- Real-Time Results: Get immediate feedback after each session, allowing for quick and effective practice.
- User-Friendly Interface: Navigate through an intuitive design that makes the preparation process straightforward and enjoyable.


## Prerequisities

- Python 3.10 +
- GCC Compiler
- CMake 3.29.0 +
- Together AI API Key
- Assembly AI API Key

## Build Instructions

Follow the below instructions to install the project.

1. First, clone the repository from github.
2. Then run the following commands to install necessary libraries and dependencies for the project. Run these commands in the terminal from project directory:
   ```
   pip install -r requirements.txt
   ```
3. Create .env file in project directory and add environment variables in the following format:
    ```
   TOGETHER_API_KEY="TOGETHER AI API KEY FOR LLM"
   ASSEMBLYAI_API_KEY="ASSEMBLY AI API KEY FOR Speech To Text"
   ```
4. To run the Server execute the following command in terminal from project directory:
    ```
   cd frontend && python -m streamlit run app.py
   ```
