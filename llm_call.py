import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.api_key)

def gpt4_query(prompt):
    try:
        # Make the API call to GPT-4
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract and return the response text
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
prompt = "What is the capital of France?"
result = gpt4_query(prompt)
print(f"Prompt: {prompt}")
print(f"Response: {result}")