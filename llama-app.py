import streamlit as st
import ollama

st.set_page_config(page_title="Llamaprat 🦙", page_icon="🦙")
st.title("Llamaprat 🦙")


# Chat-historikk
if "messages" not in st.session_state:
    st.session_state.messages = []


# Velg modell
if "ollama_model" not in st.session_state:
    st.session_state.ollama_model = "llama3.1"


# Funksjon for å spørre modellen
def spør_modellen(meldingar):
    try: 
        svar = ollama.chat(
            model=st.session_state.ollama_model,
            messages=meldingar
            )
        return svar["message"]["content"]
    except Exception as e:
        st.error(f"Feil i kommunikasjonen med modellen: {str(e)}")
        return None


# Vise meldingar frå chat-historikken
for melding in st.session_state.messages:
    with st.chat_message(melding["role"]):
        st.markdown(melding["content"])

# Funksjon for å tømme chat-historikken
def tøm_historikk():
    st.session_state.messages = []


# Chat input
if instruks := st.chat_input("Kva lurer du på?"):
    # legg til brukarinput i chat-historikken
    st.session_state.messages.append({"role": "user", "content": instruks})

    # Vis brukarinput i chat-melding-boksen
    with st.chat_message("user"):
        st.markdown(instruks)

    # Vis svar frå Llama i chat-melding-boksen
    with st.chat_message("assistant"):
        with st.spinner("Tenkjer..."):
            svar = spør_modellen(st.session_state.messages)
            if svar:
                st.markdown(svar)
                st.session_state.messages.append({"role": "assistant", "content": svar})


# Sidepanel
st.sidebar.title("Innstillingar")
st.sidebar.markdown("Denne appen nyttar ein lokal llama 3.1 8b modell")

# Legg til en knapp for å tømme chathistorikken
if st.sidebar.button("Tøm chat-historikk"):
    tøm_historikk()

# Vis antall meldinger i chat-historikken (for debugging)
st.sidebar.write(f"Antall meldinger i historikken: {len(st.session_state.messages)}")

# Vis modellnavn
st.sidebar.write(f"Aktiv modell: {st.session_state.ollama_model}")

# For debugging: Vis innholdet i meldingshistorikken
st.sidebar.write("Meldingshistorikk:")
for i, msg in enumerate(st.session_state.messages):
    st.sidebar.write(f"{i+1}. {msg['role']}: {msg['content'][:50]}...")