# IELTS-Helper_TeamSpeakPro


## Description

TODO: Need to be filled


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