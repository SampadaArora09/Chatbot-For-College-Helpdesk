import streamlit as st
import nltk
import random

# Download punkt tokenizer (only the first time)
nltk.download('punkt', quiet=True)

# --- Dataset: your college Q&A ---
qa_pairs = {
    "What are the college timings?": "The college timings are from 9 AM to 5 PM.",
    "Where is the admin office?": "The admin office is in the Dome Building.",
    "What are the courses offered here?": "We offer B.Tech, BBA, BCA, and MSc programs.",
    "How to contact admin?": "You can contact the admin office at admin@college.edu or call 0123-4567890.",
    "What is the attendance policy": "Students must maintain at least 75% attendance to appear for exams.",
    "Is there any entrance exam?":"Yes there is one called MET.",
    "What is the location of college?":"The address of college is:Manipal University Jaipur, Dehmi Kalan, Off Jaipur-Ajmer Expressway, Jaipur, Rajasthan, 303007",
    "What is the NIRF ranking of college?":"58th in the University category by NIRF in 2025",
    "What is the average package?":"The average package is INR 8.5 LPA",
    "When was the college established?":"2011" 
}

# --- Greetings ---
greetings = ["hi", "hello", "hey", "good morning", "good evening"]
greet_responses = [
    "Hello! How can I help you today?",
    "Hi there! Need some information?",
    "Hey! What do you want to know about the college?"
]
#  main logic
from difflib import SequenceMatcher, get_close_matches

def check_greeting(sentence):
    for word in sentence.split():
        if word.lower() in greetings:
            return random.choice(greet_responses)
    return None


def find_best_match(user_input, questions):
    """Returns the closest matching question using similarity."""
    best_match = get_close_matches(user_input, questions, n=1, cutoff=0.3)
    if best_match:
        return best_match[0]
    return None


def get_response(user_input):
    user_input = user_input.lower()

    # Check greeting first
    greeting = check_greeting(user_input)
    if greeting:
        return greeting

    questions = list(qa_pairs.keys())

    # Find closest matching question
    best_match = find_best_match(user_input, questions)

    if best_match:
        return qa_pairs[best_match]

    # Fallback
    return "Sorry, I don't have information on that. Could you ask in a different way?"


# Streamlit UI 
st.set_page_config(page_title="🎓 College Helpdesk Chatbot", layout="centered")

st.title("🎓 College Helpdesk Chatbot")
st.write("Ask me anything related to your college, and I'll try to help you!")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input box
user_input = st.text_input("Type your question here 👇")

# When user enters something
if user_input:
    bot_response = get_response(user_input)
    
    # Save conversation
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

# Display chat history
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f" **You:** {msg}")
    else:
        st.markdown(f" **Bot:** {msg}")


