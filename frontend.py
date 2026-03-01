import streamlit as st
from backend import ask_llm

st.set_page_config(page_title="ASTRALGEN", page_icon="")

st.title("ASTRALGEN – Chatbot")



if "history" not in st.session_state:
    st.session_state.history = []


for entry in st.session_state.history:
    with st.chat_message("user"):
        st.write(entry["user"])
    if "assistant" in entry:
        with st.chat_message("assistant"):
            st.write(entry["assistant"])


user_input = st.chat_input("Dit moi quelque chose ?")


if user_input:

    st.session_state.history.append({"user": user_input})

    with st.chat_message("user"):
        st.write(user_input)


    response = ask_llm(st.session_state.history)


    st.session_state.history[-1]["assistant"] = response


    with st.chat_message("assistant"):
        st.write(response)