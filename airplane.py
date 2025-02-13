import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline

# Charger le modèle sauvegardé
model = joblib.load("xgb_airplane_price_model.pkl")

# Titre de l'application
st.title("Prédiction du prix des avions")

# Avertissement important
# st.warning("""
# **Attention :** Ce modèle contient une fuite de données via la caractéristique 'Prix_par_siege' 
# qui utilise la variable cible (Prix) dans son calcul. Ceci rend les prédictions non fiables.
# Veuillez ré-entraîner le modèle après correction des fonctionnalités.
# """)

def engineer_features_input(df):
    df = df.copy()
    
    # Transformation logarithmique
    df['log_Consommation'] = np.log1p(df['Consommation de carburant (L/h)'])
    df['log_Cout_Maintenance'] = np.log1p(df['Coût de maintenance horaire ($)'])
    
    # Création de Catégorie_Capacité (identique au pipeline d'entraînement)
    bins = [0, 50, 150, np.inf]
    labels = ['Petite', 'Moyenne', 'Grande']
    df['Catégorie_Capacité'] = pd.cut(df['Capacité'], bins=bins, labels=labels)
    
    # Calcul des ratios (avec placeholder pour Prix_par_siege)
    df['Efficacite'] = df['Autonomie (km)'] / df['Consommation de carburant (L/h)']
    df['Prix_par_siege'] = 0  # Placeholder temporaire
    
    return df.drop([
        'Consommation de carburant (L/h)',
        'Coût de maintenance horaire ($)'
    ], axis=1, errors='ignore')

# Interface utilisateur
st.write("Entrez les caractéristiques de l'avion pour prédire son prix :")

col1, col2 = st.columns(2)
with col1:
    modele = st.selectbox("Modèle", options=["Bombardier CRJ200", "Airbus A320", "Boeing 737"])
    annee_production = st.number_input("Année de production", min_value=1900, max_value=2025, value=2000)
    nombre_moteurs = st.number_input("Nombre de moteurs", min_value=1, max_value=10, value=2)
    type_moteur = st.selectbox("Type de moteur", options=["Turbofan", "Turboprop", "Piston"])
    
with col2:
    capacite = st.number_input("Capacité (passagers)", min_value=1, max_value=1000, value=150)
    autonomie = st.number_input("Autonomie (km)", min_value=0, value=3000)
    consommation = st.number_input("Consommation (L/h)", min_value=0.0, value=14.36, format="%.2f")
    cout_maintenance = st.number_input("Coût maintenance ($/h)", min_value=0.0, value=2185.43, format="%.2f")
    region_vente = st.selectbox("Région de vente", options=["Asie", "Europe", "Amérique"])

# Création des données d'entrée
data_input = {
    "Modèle": [modele],
    "Année de production": [annee_production],
    "Nombre de moteurs": [nombre_moteurs],
    "Type de moteur": [type_moteur],
    "Capacité": [capacite],
    "Autonomie (km)": [autonomie],
    "Consommation de carburant (L/h)": [consommation],
    "Coût de maintenance horaire ($)": [cout_maintenance],
    "Région de vente": [region_vente],
    "Âge": [pd.Timestamp.now().year - annee_production]
}

df_input = pd.DataFrame(data_input)

try:
    # Feature engineering
    df_processed = engineer_features_input(df_input)
    
    # Vérification des caractéristiques requises
    required_features = [
        'Année de production', 'Nombre de moteurs', 'Capacité', 'Autonomie (km)',
        'log_Consommation', 'log_Cout_Maintenance', 'Âge', 'Prix_par_siege',
        'Efficacite', 'Modèle', 'Type de moteur', 'Région de vente', 'Catégorie_Capacité'
    ]
    
    missing = [f for f in required_features if f not in df_processed.columns]
    if missing:
        st.error(f"Caractéristiques manquantes : {', '.join(missing)}")
        st.stop()
    
    if st.button("Prédire le prix"):
        prediction = model.predict(df_processed)
        st.success(f"Prix prédit : ${prediction[0]:,.2f}")
        # st.info("Note : Cette prédiction n'est pas fiable en raison de la fuite de données identifiée")
        
except Exception as e:
    st.error(f"Erreur lors du traitement : {str(e)}")
    st.write("Données traitées :")
    st.dataframe(df_processed)