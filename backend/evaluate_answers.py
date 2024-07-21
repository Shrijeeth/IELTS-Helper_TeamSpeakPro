import os

from together import Together


def generate_feedback(answers):
    client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

    response = client.chat.completions.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[{"role": "user", "content": f"""Directly start your response from overall band score then Provide me personalized feedback for following ielts speaking interview, what are my weakness and what are my strength and return the result in proper markdown format, Here's the speaking module : {answers}"""}],
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>"],
        stream=False
    )
    # print(response.choices[0].message.content)
    return response.choices[0].message.content


def request_feedback():
    with open('./backend/data/Answers.txt', 'r') as file:
        ab = file.read()
    return generate_feedback(ab)
