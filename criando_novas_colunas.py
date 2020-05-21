import pandas as pd

dados = pd.read_csv('./data/aluguel_residencial_higienizado.csv', sep=';')

print('Calculando novas colunas:\n')
dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']
dados['Valor m2'] = (dados['Valor'] / dados['Area']).round(2)
dados['Valor Bruto m2'] = (dados['Valor Bruto'] / dados['Area']).round(2)

casas = ['Casa', 'Casa de Condomínio', 'Casa de Vila']

# .apply aplica uma função a todos as rows
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda value: 'Casa' if value in casas else 'Aparamento')

print(dados[['Tipo Agregado', 'Valor', 'Valor Bruto', 'Valor m2', 'Valor Bruto m2']].head())
