logo = Image.open("A_logo_for_a_sports_betting_promotional_campaign.png")
st.image(logo, use_column_width=True)
import streamlit as st

st.set_page_config(page_title="Zidel Even - Prédictions Foot", layout="centered")

# --- Titre et logo ---
st.markdown("<h1 style='text-align: center;'>⚽ Zidel Even - Prédictions Football</h1>", unsafe_allow_html=True)
st.image("https://i.imgur.com/U7XlWaN.png", width=150)  # Logo fictif

# --- Formulaire de prédiction ---
st.markdown("## 🔮 Entrez deux équipes pour générer une prédiction")
equipe1 = st.text_input("Équipe 1", placeholder="Ex: Real Madrid")
equipe2 = st.text_input("Équipe 2", placeholder="Ex: FC Barcelone")

# --- Prédire ---
if st.button("Prédire le score"):
    st.markdown("### Résultat prédit :")
    st.success(f"**{equipe1} 2 - 2 {equipe2}**")

    # Affichage de confiance et justification (fictifs)
    st.markdown("#### 📊 Statistiques utilisées :")
    st.write("- Moyenne buts marqués (5 derniers matchs)")
    st.write("- Historique confrontations")
    st.write("- Classement actuel (fictif)")

    st.markdown("#### 🔎 Justification :")
    st.info("Les deux équipes ont une attaque performante mais des défenses moyennes.")

    st.markdown("#### 🔐 Confiance : **72%**")

# --- Sidebar avec codes promo ---
st.sidebar.markdown("### 🎁 Bonus de Bienvenue")
st.sidebar.markdown("**1xBet Code Promo** : `BXBX`")
st.sidebar.markdown("**1Win Code Promo** : `BXBX01`")
st.sidebar.markdown("**Betwinner Code Promo** : `BXBX01`")
st.sidebar.markdown("[👉 S’inscrire maintenant](https://1xbet.com/fr)")

# --- Footer ---
st.markdown("---")
st.markdown("<center>App développée par Zidel Even 🔥</center>", unsafe_allow_html=True)
