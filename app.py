import streamlit as st
import openai
import textwrap

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
        prompt = textwrap.dedent(f"""
            Du bist ein Unternehmensberater. Führe eine SWOT-Analyse durch (Stärken, Schwächen, Chancen, Risiken) für folgendes Thema:

            {nutzer_input}

            Gib die Antwort bitte als klare Liste aus.
        """)
    elif modul == "Business Model Canvas":
        prompt = textwrap.dedent(f"""
            Du bist ein Unternehmensberater. Erstelle ein vollständiges Business Model Canvas (BMC) für folgendes Thema:

            {nutzer_input}

            Gib die Antwort bitte mit den klassischen BMC-Elementen aus:
            - Kundensegmente
            - Wertangebote
            - Kanäle
            - Kundenbeziehungen
            - Einnahmequellen
            - Schlüsselressourcen
            - Schlüsselaktivitäten
            - Schlüsselpartnerschaften
            - Kostenstruktur
        """)

    with st.spinner("ConsultantGPT denkt nach ..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du bist ein professioneller Business Consultant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        antwort = response.choices[0].message.content

    st.subheader("Dein Ergebnis:")
    st.markdown(antwort)

st.markdown("---")
st.caption("ConsultantGPT MVP | Erstellt von Osman Sahbaz")
