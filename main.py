import pandas as pd

arquivo = 'datasets/movies/Highest Holywood Grossing Movies.csv'

# Carrega o dataset
df = pd.read_csv(arquivo)

# Mostra as primeiras linhas do dataset
df.head(10)

# Mostra as colunas do dataset
#print(df.columns)