import streamlit as st
import random

st.set_page_config(page_title="Zidel Even - Prédictions Foot", layout="centered")

st.title("⚽ Prédictions de Matchs de Football")
st.markdown("Entrez deux équipes pour générer une prédiction.")

team1 = st.text_input("Équipe 1")
team2 = st.text_input("Équipe 2")

if st.button("🔮 Prédire le score"):
    if team1 and team2:
        score1 = random.randint(0, 4)
        score2 = random.randint(0, 4)

        st.success(f"Résultat prédit : **{team1} {score1} - {score2} {team2}**")
        st.info("Confiance : 68% · Justification : forme fictive des équipes.")
    else:
        st.warning("Veuillez entrer les deux équipes.")
