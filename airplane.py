import streamlit as st
import joblib
import pandas as pd

# Charger le modèle sauvegardé
model = joblib.load("xgb_airplane_price_model.pkl")

# Titre de l'application
st.title("Prédiction du prix des avions")

st.write("Entrez les caractéristiques de l'avion pour prédire son prix :")

# Saisie des paramètres numériques
annee_production = st.number_input("Année de production", min_value=1900, max_value=2025, value=2000)
nombre_moteurs = st.number_input("Nombre de moteurs", min_value=1, max_value=10, value=2)
capacite = st.number_input("Capacité (nombre de passagers)", min_value=1, max_value=1000, value=150)
autonomie = st.number_input("Autonomie (km)", min_value=0, value=3000)
consommation = st.number_input("Consommation de carburant (L/h)", min_value=0.0, value=14.36, format="%.2f")
cout_maintenance = st.number_input("Coût de maintenance horaire ($)", min_value=0.0, value=2185.43, format="%.2f")
age = st.number_input("Âge (années)", min_value=0, max_value=100, value=36)

# Saisie des paramètres catégoriels
# Remplacer les options par celles correspondant à votre dataset réel
modele = st.selectbox("Modèle", options=["Bombardier CRJ200", "Airbus A320", "Boeing 737"])
type_moteur = st.selectbox("Type de moteur", options=["Turbofan", "Turboprop", "Piston"])
region_vente = st.selectbox("Région de vente", options=["Asie", "Europe", "Amérique"])

# Créer un DataFrame avec les données saisies
data_input = {
    "Modèle": [modele],
    "Année de production": [annee_production],
    "Nombre de moteurs": [nombre_moteurs],
    "Type de moteur": [type_moteur],
    "Capacité": [capacite],
    "Autonomie (km)": [autonomie],
    "Consommation de carburant (L/h)": [consommation],
    "Coût de maintenance horaire ($)": [cout_maintenance],
    "Âge": [age],
    "Région de vente": [region_vente]
}
df_input = pd.DataFrame(data_input)

# Bouton de prédiction
if st.button("Prédire le prix"):
    prediction = model.predict(df_input)
    st.success(f"Le prix prédit de l'avion est : ${prediction[0]:,.2f}")
