from openai import OpenAI

client = OpenAI(api_key="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx") 

def call_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI hiring assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error calling OpenAI API: {e}"








