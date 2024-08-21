# lokal-ai-app

Tester litt python, KI og Ollama. 
Lokale modellar som kan lastast ned og køyrast på maskina di. Ingen data som vert delt med andre...

## llama-app-v2.py 
er med langchain, for å enklare kunne legge til fleire modellar. Inkluderer strøyming av svar.

<img src="dømev2.png" width="75%" />

## llama-app.py
er utan langchain, og har ikkje strøyming av svar. Første versjon.

<img src="døme.png" width="75%" />


## Du treng
- **[ollama](ollama.ai)** for å lasta ned/køyra språkmodellen
    - Ein språkmodell (feks **[llama 3.1 8b](https://ollama.com/library/llama3.1)**) 
- **[Streamlit](https://streamlit.io/)** for å kjøra appen
- **[🔗 Langchain](https://python.langchain.com/v0.2/docs/introduction/)** for å enklare kunna bytta frå Ollama til feks. OpenAI etc. 

### Python - requirements

For å installera biblioteka i python (gjerne i eit conda env) kan du køyra

```bash
pip install -r requirements.txt
```