import streamlit as st
import ollama 

st.set_page_config(page_title="Llamaprat 🦙", page_icon="🦙")
st.title("Llamaprat 🦙")

# Definere modellen som skal brukast
st.session_state.model = "llama3.1"

# Sette opp chat-historikk
if "messages" not in st.session_state:
    st.session_state["messages"] = [{
        "role": "assistant", 
        "content": "Hei! Eg er ein Llama. Kva kan eg hjelpe deg med?"
    }]

# Vise meldingar frå chat-historikken
for melding in st.session_state.messages:
    if melding["role"] == "user":
        st.chat_message(melding["role"], avatar="🙋").write(melding["content"])
    else:
        st.chat_message(melding["role"], avatar="🦙").write(melding["content"])

# Chat input
if instruks := st.chat_input("Kva lurer du på?"):
    # legg til brukarinput i chat-historikken
    st.session_state.messages.append({"role": "user", "content": instruks})

    # Vis brukarinput i chat-melding-boksen
    st.chat_message("user", avatar="🙋").write(instruks)

    # Vis svar frå Llama i chat-melding-boksen
    with st.chat_message("assistant", avatar="🦙"):
        with st.spinner("Tenkjer..."):
            svar = ollama.chat(
                model = st.session_state.model,
                messages= st.session_state.messages
            )

            st.write(svar["message"]["content"])

        st.session_state.messages.append({"role": "assistant", "content": svar["message"]["content"]})