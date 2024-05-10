import openai

key = "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"

openai.api_key = key

def analyse_text(text):
    print("Analising...")
    prompt_text = "detect key words for hiring candidates for: "+text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_text}]
    )

    return (response.choices[0].message['content'])


print(analyse_text(a_text))
