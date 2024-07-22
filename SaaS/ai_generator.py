import openai

openai.api_key = 'your-openai-api-key'

def ai_generator(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()
