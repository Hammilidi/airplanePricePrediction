# Prédiction des Prix des Avions avec XGBoost

## Description du Projet
Ce projet vise à développer un modèle de machine learning capable de prédire le prix des avions en fonction de plusieurs caractéristiques telles que l'année de production, la capacité, le type de moteur, l'autonomie et les coûts d'entretien.

Le modèle choisi est **XGBoost**, un algorithme puissant de boosting d'arbres de décision, optimisé avec une recherche d'hyperparamètres.

---

## Démarches et Techniques Utilisées
### 1. **Prétraitement des Données**
- Suppression des valeurs manquantes et gestion des valeurs extrêmes.
- Transformation logarithmique des variables fortement asymétriques (prix, consommation de carburant, coût de maintenance).

### 2. **Feature Engineering**
- Ajout de nouvelles variables :
  - **log_Consommation** : Transformation logarithmique de la consommation de carburant.
  - **log_Cout_Maintenance** : Transformation logarithmique du coût de maintenance.
  - **Prix_par_siege** : Rapport entre le prix et la capacité en sièges.
  - **Efficacite** : Rapport entre l'autonomie et la consommation de carburant.

### 3. **Encodage et Standardisation**
- Encodage **One-Hot Encoding** pour les variables catégoriques.
- Normalisation des variables numériques avec **StandardScaler**.

### 4. **Modélisation avec XGBoost**
- Optimisation des hyperparamètres avec **GridSearchCV**.
- Entraînement du modèle sur 80% des données et test sur 20%.

### 5. **Métriques d'évaluation**
- **RMSE (Root Mean Squared Error)** : 2 923 850.80
- **R² (Coefficient de détermination)** : 0.9998
- **MAE (Mean Absolute Error)** : 1 054 933.99
- **MAPE (Mean Absolute Percentage Error)** : 6.21%

---

## Interprétation des Résultats
- **Le modèle est très performant**, expliquant **99.98 % de la variance des prix**.
- Une erreur moyenne de **6.21 %**, ce qui signifie que le modèle prédit avec une grande précision.
- Le tuning des hyperparamètres a permis de **réduire les erreurs et d'améliorer la généralisation**.

---

## Améliorations Possibles
1. **Analyse des erreurs résiduelles** pour identifier les segments sous-performants.
2. **Ajout de nouvelles features**, comme des données économiques influençant le prix des avions.
3. **Test d'autres modèles** en combinaison avec XGBoost (ex : LightGBM, Random Forest).

---

## Installation et Exécution
### 1. Cloner le dépôt :
```bash
git clone https://github.com/votre-repo.git
cd votre-repo
```

### 2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

### 3. Lancer le script d'entraînement :
```bash
python train.py
```

---

## Auteurs
- **Yonli Fidèle**

---

## Licence
Ce projet est sous licence MIT.

