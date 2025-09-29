import pandas as pd

df=pd.read_csv("./data/raw/assurance-maladie.csv")

# Fournit des statistiques descriptives sur les colonnes numériques
print(df.describe())

# Donne des informations générales sur le DataFrame :
    # Nombre de lignes et de colonnes
    # Nom et type de chaque colonne 
    # Nombre de valeurs non nulles(voir les données manquantes).
    # Taille mémoire utilisée.
print(df.info())

# Affiche les 5 premières lignes du DataFrame
print("Affichage",df.head())

