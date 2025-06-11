import streamlit as st
import openai

# Seiten-Setup
st.set_page_config(page_title="ConsultantGPT", layout="centered")
st.title("🤖 ConsultantGPT – Dein persönlicher Berater")

# API-Key sicher laden
oapi_key = st.secrets.get("api_key")
if not oapi_key:
    st.error("Bitte trage deinen OpenAI API-Key in die Streamlit Secrets ein.")
    st.stop()

# OpenAI-Client
client = openai.OpenAI(api_key=oapi_key)

# Auswahlmodul
modul = st.selectbox("Welches Tool möchtest du nutzen?", ["SWOT-Analyse", "Business Model Canvas"])

nutzer_input = st.text_area("Beschreibe dein Thema, Projekt oder Unternehmen:")

if st.button("Analysieren") and nutzer_input:
    if modul == "SWOT-Analyse":
        prompt = f"""
        Du bist ein Unternehmensberater. Führe eine SWOT-Analyse durch (Stärken, Schwächen, Chancen, Risiken) für folgendes Thema:

        {nutzer_input}

        Gib die Antwort bitte als klare Liste aus.
        """
    elif modul == "Business Model Canvas":
        prompt = f"""
        Du bist ein Unternehmensberater. Erstelle ein vollständiges Business Model Canvas (BMC) für folgendes Thema:

        {nutzer_in_
