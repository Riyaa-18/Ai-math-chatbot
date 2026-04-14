import streamlit as st

st.title("AI Math Assistant Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user = st.text_input("Ask your math question:")

if user:
    st.session_state.chat.append(("You", user))
    reply = "Step-by-step solution: First understand, then solve logically step by step."
    st.session_state.chat.append(("AI", reply))

for role, msg in st.session_state.chat:
    st.write(role + ":", msg)
