import streamlit as st
from openai import OpenAI

st.title("AI Math Assistant Chatbot 🤖")

# SAFE CHECK (IMPORTANT)
if "OPENAI_API_KEY" not in st.secrets:
    st.error("API Key missing in Streamlit Secrets!")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "chat" not in st.session_state:
    st.session_state.chat = []

user = st.text_input("Ask your math question:")

if user:
    st.session_state.chat.append(("You", user))

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful math tutor. Explain step by step."},
                {"role": "user", "content": user}
            ]
        )

        reply = response.choices[0].message.content

    except Exception as e:
        reply = f"Error from API: {e}"

    st.session_state.chat.append(("AI", reply))

for role, msg in st.session_state.chat:
    st.write(f"{role}: {msg}")
