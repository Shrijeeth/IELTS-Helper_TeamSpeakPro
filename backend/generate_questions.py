import os

from together import Together


def generate_part1():
    client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

    stream = client.chat.completions.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[{"role": "user", "content": """Do not include any starting lines like "here's the question" or anything else.Provide me IELTS Part One of the speaking module with random questions. Provide only the questions, nothing else. Include two general lines like "What's your name?" and "What do you do?" followed by 7-8 random questions for Part One."""}],
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>"],
        stream=True
    )
    # print(response.choices[0].message.content)
    with open("./backend/data/Question_for_part01.txt", "w") as file:
        for chunk in stream:
            if hasattr(chunk.choices[0].delta, 'content'):
                content = chunk.choices[0].delta.content
                # print(content, end="", flush=True)
                file.write(content)


def generate_part2(previous_topic):
    client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

    stream = client.chat.completions.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[{"role": "user", "content": f"""Do not include any starting lines like "here's the topic" or don't add description about topic and anything else.Generate a random IELTS Part Two speaking that is completely different from {previoustopic} with maximum leangth of 6,7 words, very short like 1 sentance, 3,4 bulit question and at the end add line "You have 1 minute to prepare, and then you will speak for 2 minutes."."""}],
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>"],
        stream=True
    )
    # print(response.choices[0].message.content)
    with open("./backend/data/Question_for_part02.txt", "w") as file:
        for chunk in stream:
            if hasattr(chunk.choices[0].delta, 'content'):
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                file.write(content)


def load_questions(file_path):
    with open(file_path, "r") as file:
        raw_lines = file.readlines()
    cleaned_lines = [line.strip() for line in raw_lines if line.strip()]
    return cleaned_lines
