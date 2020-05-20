import pandas as pd

dados = pd.read_csv('./data/aluguel_residencial.csv', sep=';')

# n1 = dados[dados['Tipo'] == 'Apartamento']
n1 = dados.query("Tipo == 'Apartamento'")

# n2 = dados.query("Tipo == 'Casa' or Tipo == 'Casa de Condomínio' or Tipo == 'Casa de Verão'")
# n2 = dados.query("Tipo in ['Casa', 'Casa de Condomínio', 'Casa de Verão']")
n2 = dados[dados['Tipo'].isin(['Casa', 'Casa de Condomínio', 'Casa de Verão'])]

n3 = dados.query("Area >= 60 and Area <= 100")
n4 = dados.query("Quartos >= 4 and Valor < 2000.0")



