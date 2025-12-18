from groq import Groq
from pathlib import Path

# =====================================================
# Chemin de base du projet
# =====================================================
BASE_DIR = Path(__file__).resolve().parent


# =====================================================
# Lecture de la clé API depuis cleapi.txt
# =====================================================
import os

def get_api_key():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("❌ La clé API GROQ_API_KEY n'est pas définie dans les secrets Streamlit.")
    return api_key


# =====================================================
# Lecture du prompt système
# =====================================================
def read_file(file_name):
    return (BASE_DIR / file_name).read_text(encoding="utf-8")


# =====================================================
# Construction des messages
# =====================================================
def build_messages(history):
    messages = [
        {
            "role": "system",
            "content": read_file("context.txt")
        }
    ]

    for entry in history:
        messages.append({"role": "user", "content": entry["user"]})
        if "assistant" in entry:
            messages.append({"role": "assistant", "content": entry["assistant"]})

    return messages


# =====================================================
# Appel au LLM
# =====================================================
def ask_llm(history):
    api_key = get_api_key()
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=build_messages(history)
    )

    return response.choices[0].message.content


# =====================================================
# Test local
# =====================================================
if __name__ == "__main__":
    test_history = [{"user": "Bonjour, qui es-tu ?"}]
    print(ask_llm(test_history))
