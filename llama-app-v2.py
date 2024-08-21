import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# config
st.set_page_config(page_title="Llamaprat 🦙", page_icon="🦙")
st.title("Llamaprat 2.0🦙")
st.markdown("**modell:** llama3.1 (8b)")
st.markdown("Bruker 🔗Langchain for å lettare kunna bytta modell seinare.")
st.markdown("---")

# funksjon for å hente svar frå modellen
def få_svar(user_question, chat_history):

    template = """
    You are a helpful assistant. Answer the following questions short and precisely considering the history of the conversation:

    Chat history: {chat_history}

    User question: {user_question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOllama(model="llama3.1")
        
    chain = prompt | llm | StrOutputParser()
    
    return chain.stream({
        "chat_history": chat_history,
        "user_question": user_question,
    })

# Session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        AIMessage("Hei! Eg er ein Llama. Kva kan eg hjelpe deg med?")
    ]


# chatten
for melding in st.session_state.chat_history:
    if isinstance(melding, AIMessage):
        with st.chat_message("AI", avatar="🦙"):
            st.write(melding.content)
    else:
        with st.chat_message("Human", avatar="🙋"):
            st.write(melding.content)


# brukarinput
if user_question := st.chat_input("Kva lurer du på?"):
    st.session_state.chat_history.append(HumanMessage(content=user_question))

    with st.chat_message("Human", avatar="🙋"):
        st.write(user_question)

    with st.chat_message("AI", avatar="🦙"):
        with st.spinner("Tenkjer..."):
            svar = st.write_stream(få_svar(user_question, st.session_state.chat_history))
    
    st.session_state.chat_history.append(AIMessage(content=svar))


