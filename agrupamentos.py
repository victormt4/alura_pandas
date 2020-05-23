import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('./data/aluguel_residencial_sem_valor_bruto.csv', sep=';')

bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
select = dataset['Bairro'].isin(bairros)
sub_dataset = dataset[select]

group_bairro = sub_dataset.groupby('Bairro')

# for group, data_frame in group_bairro:
#     print(f"Bairro: {group} - Media: {data_frame['Valor'].mean()}")

print('\nMedia por bairro:\n')
print(group_bairro[['Valor', 'Condominio']].mean().round(2))

print('\nEstatísticas descritivas por bairro:\n')
print(group_bairro['Valor'].describe().round(2))
print(group_bairro['Valor']
      .aggregate(['min', 'max', 'sum'])
      .rename(columns={'min': 'Mínimo', 'max': 'Máximo', 'sum': 'Total'}))

# Gráficos
#plt.rc('figure', figsize=(20, 10))  # Configurando tamanho

# group_bairro = dataset.groupby('Bairro')

group_bairro['Valor'].std().plot.bar()
plt.show()
