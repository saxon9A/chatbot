import streamlit as st
from backend import ask_llm

st.set_page_config(page_title="Rayan-CHATBOT", page_icon="🧭")

st.title("🧭 Rayan – Chatbot")



# INITIALISATION DE LA MEMOIRE
if "history" not in st.session_state:
    st.session_state.history = []


# AFFICHAGE DE L'HISTORIQUE
for entry in st.session_state.history:
    with st.chat_message("user"):
        st.write(entry["user"])
    if "assistant" in entry:
        with st.chat_message("assistant"):
            st.write(entry["assistant"])


# INPUT UTILISATEUR
user_input = st.chat_input("Écris ici pour parler avec ton Cartographe des Idées...")


if user_input:
    # On ajoute le message de l’user dans la mémoire
    st.session_state.history.append({"user": user_input})

    # AFFICHAGE IMMÉDIAT
    with st.chat_message("user"):
        st.write(user_input)

    # REQUÊTE AU LLM
    response = ask_llm(st.session_state.history)

    # Stockage de la réponse dans l’historique
    st.session_state.history[-1]["assistant"] = response

    # AFFICHAGE RÉPONSE
    with st.chat_message("assistant"):
        st.write(response)