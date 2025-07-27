 import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Zidel Even - Prédictions Football")

st.title("📊 Prédictions Football - 26 Juillet 🇷🇺")
st.markdown("**By Zidel Even | Avec les codes promo 🔥**")
st.markdown("- **1xbet : BXBX**")
st.markdown("- **Betwinner : BXBX01**")
st.markdown("- **1win : BXBX01**")
st.markdown("---")

# Vérifie si le fichier existe
csv_path = "matchs_demo.csv"

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)

    for i, row in df.iterrows():
        st.markdown(f"### {row['match']}")
        st.markdown(f"**🟩 Pronostic :** `{row['pronostic']}`")
        st.markdown(f"**📊 Confiance :** {row['confiance']}%")
        st.markdown("---")
else:
    st.error(f"❌ Le fichier `{csv_path}` est introuvable.\n\n💡 Solution : ajoute-le à ton dépôt GitHub.")
