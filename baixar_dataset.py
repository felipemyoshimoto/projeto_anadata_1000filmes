import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Inicia a API do kaggle
api = KaggleApi()
api.authenticate()

# Define o dataset (exemplo: top 1000 highest grossing movies)
dataset = "sanjeetsinghnaik/top-1000-highest-grossing-movies"

# Pasta onde vai salvar os dados
save_path = 'datasets/movies'
os.makedirs(save_path, exist_ok=True)

# Baixa e descompacta o dataset
api.dataset_download_files(dataset, path=save_path, unzip=True)

print(f"Dataset baixado em: {save_path}")
