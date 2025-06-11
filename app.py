
import streamlit as st
import openai

# Seiten-Setup
st.set_page_config(page_title="ConsultantGPT", layout="centered")
st.title("🤖 ConsultantGPT - Dein persönlicher Berater")

# API-Key sicher laden
oapi_key = st.secrets.get("api_key")
if not oapi_key:
    st.error("Bitte trage deinen OpenAI API-Key in die Streamlit Secrets ein.")
    st.stop()

openai.api_key = oapi_key

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
        """

    with st.spinner("ConsultantGPT denkt nach ..."):
       client = openai.OpenAI(api_key=oapi_key)

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "..."},
        {"role": "user", "content": "..."}
    ],
    temperature=0.7
)
antwort = response.choices[0].message.content
        st.subheader("Dein Ergebnis:")
        st.markdown(antwort)

st.markdown("---")
st.caption("ConsultantGPT MVP | Erstellt von Osman Sahbaz")
