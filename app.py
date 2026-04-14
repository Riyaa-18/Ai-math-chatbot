import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("AI Math Assistant Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user = st.text_input("Ask your math question:")

if user:
    st.session_state.chat.append(("You", user))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user}]
    )

    reply = response.choices[0].message.content

    st.session_state.chat.append(("AI", reply))

for role, msg in st.session_state.chat:
    st.write(role + ":", msg)
