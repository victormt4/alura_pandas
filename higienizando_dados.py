import pandas as pd

dados = pd.read_csv('./data/aluguel_residencial.csv', sep=';')

print('Registros com Valor de aluguel null:\n')
print(dados[dados['Valor'].isnull()].shape)

# Higienizando dados, removendo e tratando nulos
dados.dropna(subset=['Valor'], inplace=True)  # registros sem aluguel
select = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())  # apartamento sem valor de condomínio
dados = dados[~select]  # invertendo seleção
dados = dados.fillna({'Condominio': 0, 'IPTU': 0})  # preenchendo os valores nulos restantes com 0

dados.to_csv('./data/aluguel_residencial_higienizado.csv', sep=';', index=False)
