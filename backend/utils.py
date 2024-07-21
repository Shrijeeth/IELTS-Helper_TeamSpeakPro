def save_text_to_file(filename, text, question_statement):
    try:
        print(question_statement, text)
        with open("./backend/data/" + filename, 'a+') as file:
            file.write(f"Question: {question_statement}\n")
            file.write(f"Answer: {text}\n\n")
        return True
    except Exception as e:
        print(e)
        return False


def create_file(filename):
    try:
        with open("./backend/data/" + filename, 'w') as file:
            file.write("")
        return True
    except Exception as e:
        print(e)
        return False
