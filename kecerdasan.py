import openai

openai.api_key = "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"

while True:
    model_engine = "text-davinci-003"

    prompt = input('ketik pertanyaan anda : ')

    if 'exit' in prompt or 'quit' in prompt:
        break

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text

    print(response)