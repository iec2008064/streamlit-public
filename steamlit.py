import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def process_text(text):
    # This is a placeholder function. Replace with your actual processing logic.
    return f"Processed: {text.upper()}"


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

def main():
    st.title("Ask me anything")

    # Create a text input and a button
    col1, col2 = st.columns([3, 1])
    with col1:
        user_input = st.text_input("Enter your question here:")
    with col2:
        submit_button = st.button("Submit")

    # When the submit button is clicked, call the process_text function
    if submit_button:
        if user_input:
            result = gpt4_query(user_input)
            st.write(result)
        else:
            st.warning("Please enter some text before submitting.")

if __name__ == "__main__":
    main()
