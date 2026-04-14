import streamlit as st
from openai import OpenAI

# Get API key safely from Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI Math Assistant Chatbot 🤖")

# session memory
if "chat" not in st.session_state:
    st.session_state.chat = []

# input box
user = st.text_input("Ask your math question:")

if user:
    st.session_state.chat.append(("You", user))

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful math tutor. Always explain step-by-step."},
                {"role": "user", "content": user}
            ]
        )

        reply = response.choices[0].message.content

    except Exception as e:
        reply = "Error: API key not set or invalid. Please check Streamlit Secrets."

    st.session_state.chat.append(("AI", reply))

# display chat
for role, msg in st.session_state.chat:
    st.write(f"**{role}:** {msg}")
