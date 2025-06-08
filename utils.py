import openai

openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your actual key

def call_llm(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # ✅ use this model
            messages=[
                {"role": "system", "content": "You are a helpful AI hiring assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"❌ Error calling OpenAI API: {e}"








