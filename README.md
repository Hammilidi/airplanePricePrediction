# Prédiction du Prix des Avions avec Machine Learning

## Description du Projet
Ce projet utilise l'apprentissage automatique pour prédire le prix des avions en fonction de divers paramètres. Un modèle de régression a été entraîné sur un ensemble de données contenant les prix historiques des avions. Une application web interactive a été développée avec Streamlit pour permettre aux utilisateurs de faire des prédictions en entrant les caractéristiques de l'avion.

## Fonctionnalités
- Prétraitement des données et analyse exploratoire
- Entraînement d'un modèle de régression
- Sauvegarde et chargement du modèle ML
- Interface utilisateur avec Streamlit
- Prédiction en temps réel des prix des avions

## Technologies Utilisées
- Python
- Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Pickle (pour la sauvegarde du modèle)

## Installation
### 1. Cloner le dépôt
```bash
git clone https://github.com/votre-repo/prediction-prix-avions.git
cd prediction-prix-avions
```

### 2. Créer et activer un environnement virtuel
#### Sous Windows :
```powershell
python -m venv monenv
monenv\Scripts\Activate.ps1
```
#### Sous Mac/Linux :
```bash
python3 -m venv monenv
source monenv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Utilisation
### 1. Entraîner le modèle
Exécutez le script pour entraîner et sauvegarder le modèle :
```bash
python train_model.py
```

### 2. Lancer l'application Streamlit
Démarrez l'interface utilisateur pour faire des prédictions :
```bash
streamlit run app.py
```

## Structure du Projet
```
project/
│── data/                 # Dossier contenant les données
│── models/               # Dossier pour stocker le modèle entraîné
│── app.py                # Application Streamlit
│── train_model.py        # Script d'entraînement du modèle
│── requirements.txt      # Liste des dépendances
│── README.md             # Documentation du projet
```

## Auteur
Yonli Fidèle

## Licence
Ce projet est sous licence MIT.

