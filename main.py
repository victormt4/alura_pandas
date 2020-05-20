import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('./data/aluguel.csv', sep=';')

tipos_imoveis = pd.DataFrame(dataset['Tipo'].drop_duplicates())
tipos_imoveis.index = range(tipos_imoveis.shape[0])  # refazendo índice
tipos_imoveis.columns.name = 'id'  # renomeando coluna

tipos_residenciais = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']

# Filtrando resultados
dados_residenciais = dataset[dataset['Tipo'].isin(tipos_residenciais)]

dados_residenciais.index = range(dados_residenciais.shape[0])