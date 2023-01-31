import openai

openai.api_key = "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"
conversation = ""

i = 1

while i != 0:
    questions = input("Humano:")
    conversation += "\nHumano" + questions + "\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=conversation, temperature=0.9, max_tokens=150, top_p=1.0,
        frequency_penalty=0.6, presence_penalty=0.6, stop=["\n," "humano", "AI"])
    answer = response["choices"][0]["text"]

    conversation += answer

    print("AI" + answer + "\n")