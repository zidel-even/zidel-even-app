import streamlit as st
import pandas as pd

st.set_page_config(page_title="Zidel Even ⚽", layout="centered")

st.title("📊 Prédictions Football - 26 Juillet 🇷🇺")
st.markdown("**By Zidel Even | Avec les codes promo 🔥**")
-st.markdown("- **1xbet : BXBX**")
st.markdown("- **Betwinner : BXBX01**")
st.markdown("- **1win : BXBX01**")
-  
- 

df = pd.read_csv("matchs_demo.csv")

for i, row in df.iterrows():
    st.markdown(f"### {row['match']}")
    st.markdown(f"**🟩 Pronostic : `{row['pronostic']}`**")
    st.markdown(f"- ⏰ Heure : `{row['heure']}`")
    st.markdown(f"- ⚔️ Justification : {row['justification']}")
    st.markdown(f"- 💰 Cote : `{row['cote']}`")
    st.markdown(f"- 📈 Confiance : `{row['confiance']}`")
    st.markdown("---")
