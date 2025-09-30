import pandas as pd

df=pd.read_csv("./data/raw/assurance-maladie.csv")

# Donne des informations générales sur le DataFrame :
    # Nombre de lignes et de colonnes
    # Nom et type de chaque colonne 
    # Nombre de valeurs non nulles(voir les données manquantes).
    # Taille mémoire utilisée.
df.info()

# Affiche les 5 premières lignes du DataFrame
df.head()

# Fournit des statistiques descriptives sur les colonnes numériques
df.describe()

# # Nombre de valeurs non nulles
df['age'].count()

# # Nombre de valeurs manquantes
df['age'].isnull().sum()

# Nombre de valeurs distinctes
df['age'].unique()
