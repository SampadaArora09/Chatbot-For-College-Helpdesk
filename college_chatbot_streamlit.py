import streamlit as st
import nltk
import random

# Download punkt tokenizer (only the first time)
nltk.download('punkt', quiet=True)

# --- Dataset: your college Q&A ---
qa_pairs = {
    "college timings": "The college timings are from 9 AM to 5 PM.",
    "admin office": "The admin office is in the Dome Building.",
    "courses": "We offer B.Tech, BBA, BCA, and MSc programs.",
    "contact admin": "You can contact the admin office at admin@college.edu or call 0123-4567890.",
    "attendance policy": "Students must maintain at least 75% attendance to appear for exams."
}

# --- Greetings ---
greetings = ["hi", "hello", "hey", "good morning", "good evening"]
greet_responses = [
    "Hello! How can I help you today?",
    "Hi there! Need some information?",
    "Hey! What do you want to know about the college?"
]

# --- Greeting check function ---
def check_greeting(sentence):
    for word in sentence.split():
        if word.lower() in greetings:
            return random.choice(greet_responses)
    return None

# --- Main chatbot logic ---
def get_response(user_input):
    user_input = user_input.lower()
    greeting = check_greeting(user_input)
    if greeting:
        return greeting

    for key in qa_pairs.keys():
        if key in user_input:
            return qa_pairs[key]
    return "Sorry, I don't have information on that. Please contact the admin office for help."

# --- Streamlit UI ---
st.set_page_config(page_title="🎓 College Helpdesk Chatbot", layout="centered")

st.title("🎓 College Helpdesk Chatbot")
st.write("Ask me anything about your college!")

# Input box
user_input = st.text_input("You:", "")

# Display bot response
if user_input:
    response = get_response(user_input)
    st.markdown(f"** Bot:** {response}")
