import os

from together import Together


def evaluate_speech(question, user_input):
    client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

    response = client.chat.completions.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[
            {
                "role": "system",
                "content": f"""You are an Ielts examiner and you need to grade the following speech by user for given question inside `Question` field.
Emphasize varied vocabulary, accurate spelling, and proper word formation and give suggestions to improve the speech for the given question.
Sample Output:
```
## Task Achievement:\nThe candidate has adequately addressed the task by presenting a clear stance on the topic and providing relevant arguments.
```
{question}
""",
            },
            {
                "role": "user",
                "content": user_input,
            }
        ],
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


def load_answers(file_path):
    with open(file_path, "r") as file:
        raw_data = file.read()
    question_answer_pairs = raw_data.split("\n\n")
    result = {}
    for qa in question_answer_pairs:
        qa_data = qa.split("\n")
        if len(qa_data) < 1:
            continue
        elif len(qa_data) == 1:
            result[qa_data[0]] = ""
        elif len(qa_data) == 2:
            result[qa_data[0]] = qa_data[1]
        else:
            result[qa_data[0]] = "\n".join(qa_data[1:])
    return result
