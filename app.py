import streamlit as st
import math

st.title("AI Math Assistant Chatbot 🤖 (Smart Calculator)")

if "chat" not in st.session_state:
    st.session_state.chat = []

def solve_math(user):
    try:
        # SAFE MATH ENVIRONMENT
        allowed_names = {
            "sqrt": math.sqrt,
            "pow": pow,
            "abs": abs,
            "round": round
        }

        # evaluate expression safely
        result = eval(user, {"__builtins__": None}, allowed_names)
        return f"Answer: {result}"

    except:
        # algebra formulas
        if user.strip() == "(a+b)^2":
            return "a² + 2ab + b²"
        if user.strip() == "(a-b)^2":
            return "a² - 2ab + b²"
        if user.strip() == "a^2-b^2":
            return "(a-b)(a+b)"

        return "Try: 4+6, 10-3, 5*6, 10/2, sqrt(16), pow(2,3)"

user = st.text_input("Ask your math question:")

if user:
    st.session_state.chat.append(("You", user))

    reply = solve_math(user)

    st.session_state.chat.append(("AI", reply))

for role, msg in st.session_state.chat:
    st.write(f"{role}: {msg}")
