import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def stream_gpt_response(prompt):
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
            stream=True  # Enable streaming
        )

        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"   
