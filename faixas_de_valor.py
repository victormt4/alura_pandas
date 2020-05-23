import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('./data/aluguel_residencial_sem_valor_bruto.csv', sep=';')

faixas = [0, 2, 4, 6, 100]
labels = ['0 a 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 ou mais quartos']
quartos = pd.cut(dataset['Quartos'], faixas, labels=labels, include_lowest=True)

freq_quartos = pd.value_counts(quartos)
print(freq_quartos)

print('\nAdicionando nova coluna:\n')

dataset['Faixa Quartos'] = quartos

# def map_quartos(qntd_quartos):
#     faixa = ''
#     if qntd_quartos <= 2:
#         faixa = '0 à 2 quartos'
#     elif qntd_quartos <= 4:
#         faixa = '3 e 4 quartos'
#     elif qntd_quartos <= 6:
#         faixa = '5 e 6 quartos'
#     else:
#         faixa = '7 ou mais quartos'
#
#     return faixa
#
#
# dataset['Faixa Quartos'] = dataset['Quartos'].apply(map_quartos)

dataset['Faixa Quartos'].value_counts().plot.bar()
plt.show()
