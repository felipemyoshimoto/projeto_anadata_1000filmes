🎬 Análise de Dados - 1000 Filmes de Hollywood






Este projeto explora dados de 1000 filmes de Hollywood para prática de análise de dados, limpeza de dados, cálculo de KPIs e visualização gráfica. O dataset foi obtido utilizando a API do Kaggle, garantindo que os dados estejam atualizados.

📂 Estrutura do Projeto

datasets/movies/: CSV original dos filmes, baixado via API do Kaggle.

notebooks/Hollywood_Analysis.ipynb: notebook principal com a análise.

README.md: este arquivo.

🎯 Objetivos

Carregar o dataset dos filmes em um DataFrame do pandas.

Limpar dados e tratar valores não numéricos ou ausentes.

Calcular KPIs como Lucro (Profit) e Retorno sobre Investimento (ROI).

Converter valores monetários para bilhões de dólares.

Visualizar os dados em tabelas interativas e gráficos:

Receita vs Orçamento

Receita média por gênero

Destacar os filmes mais lucrativos.

⚙️ Tecnologias

Python 3

Pandas

Matplotlib

Jupyter Notebook / VSCode

Kaggle API (para download do dataset)

📌 Observações

Alguns filmes podem ter valores ausentes ou não divulgados (ex.: orçamento de "Avatar: The Way of Water").

Estes casos são tratados no notebook, podendo ser deixados como NaN ou preenchidos com estimativas.

🚀 Como Executar

Instale as bibliotecas necessárias: Pandas, Matplotlib e Jupyter.

Configure a Kaggle API caso queira baixar o dataset diretamente.

Abra o Jupyter Notebook no VSCode ou navegador.

Navegue até Hollywood_Analysis.ipynb e execute as células para reproduzir a análise.

Este projeto está em desenvolvimento para estudo e prática de análise de dados aplicada a filmes de Hollywood, integrando limpeza de dados, cálculo de KPIs e visualizações interativas.