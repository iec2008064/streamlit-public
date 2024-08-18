import streamlit as st

def process_text(text):
    # This is a placeholder function. Replace with your actual processing logic.
    return f"Processed: {text.upper()}"

def main():
    st.title("Gaurav's personal app")

    # Create a text input and a button
    col1, col2 = st.columns([3, 1])
    with col1:
        user_input = st.text_input("Enter your text here:")
    with col2:
        submit_button = st.button("Submit")

    # When the submit button is clicked, call the process_text function
    if submit_button:
        if user_input:
            result = process_text(user_input)
            st.write(result)
        else:
            st.warning("Please enter some text before submitting.")

if __name__ == "__main__":
    main()
