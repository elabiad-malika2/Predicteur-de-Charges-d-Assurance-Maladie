import pandas as pd

df=pd.read_csv("./data/raw/assurance-maladie.csv")

# Fournit des statistiques descriptives sur les colonnes numériques
print(df.describe())


