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


def stream_gpt_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
        stream=True  # Enable streaming
    )

    st.write(response)




def main():
    # Set page configuration
    st.set_page_config(page_title="Ask Me Anything", layout="wide", initial_sidebar_state="auto")

    # Custom title with orange color
    st.markdown('<h1 style="color:orange;">Ask Me Anything - Powered by GPT</h1>', unsafe_allow_html=True)
    
    # Create a form so that pressing Enter triggers form submission
    with st.form(key='ask_me_anything_form'):
        col1, col2 = st.columns([5, 1])
        with col1:
            # Custom label with dynamic font size
            st.markdown(f'<p style="font-size:18px;">Enter your question here:</p>', unsafe_allow_html=True)
            user_input = st.text_input("", key="user_input")
        with col2:
            st.write("")  # Adding an empty write to vertically align the button
            st.write("") 
            st.write("") 
            st.write("")  # Adding an empty write to vertically align the button
            submit_button = st.form_submit_button("Submit")

    # When the submit button is clicked, call the process_text function
    if submit_button:
        if user_input:
           stream_gpt_response(user_input) 

        else:
            st.warning("Please enter some text before submitting.")

if __name__ == "__main__":
    main()
