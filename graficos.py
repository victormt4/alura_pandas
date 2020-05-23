import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('./data/aluguel_residencial_sem_outliers.csv', sep=';')

area = plt.figure()
g1 = area.add_subplot(2, 2, 1)  # 2 linhas, 2 colunas na posição 1
g2 = area.add_subplot(2, 2, 2)
g3 = area.add_subplot(2, 2, 3)
g4 = area.add_subplot(2, 2, 4)

g1.scatter(dataset['Valor'], dataset['Area'])
g1.set_title('Valor X Área')

g2.hist(dataset['Valor'])
g2.set_title('Histograma')

dataset_g3 = dataset['Valor'].sample(100)  # selecionando 100 registros aleatoriamente
dataset_g3.index = range(dataset_g3.shape[0])  # refazendo índices
g3.plot(dataset_g3)
g3.set_title('Amostra (Valor)')

group = dataset.groupby('Tipo')['Valor']
label = group.mean().index
data = group.mean().values
g4.bar(label, data)
g4.set_title('Valor Médio por Tipo')

# plt.show()

area.savefig('graficos.png', dpi=300, bbox_inches='tight')
