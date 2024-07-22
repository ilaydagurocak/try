import openai

openai.api_key = 'your-openai-api-key'

def ai_humanizer(text):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Paraphrase the following text to make it sound human-written while retaining the original meaning:\n\n{text}",
        max_tokens=500
    )
    return response.choices[0].text.strip()
