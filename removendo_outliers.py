import pandas as pd
import matplotlib.pyplot as plt


def get_stats(series):
    series_Q1 = series.quantile(.25)
    series_Q3 = series.quantile(.75)
    series_IIQ = series_Q3 - series_Q1

    return (
        series_Q1,  # primeiro quartil
        series_Q3,  # terceiro quartil
        series_IIQ,  # intervalo interquarti
        series_Q1 - (1.5 * series_IIQ),  # limite inferior
        series_Q3 + (1.5 * series_IIQ)  # limite superior
    )


dataset = pd.read_csv('./data/aluguel_residencial_sem_valor_bruto.csv', sep=';')

# Removendo outliers
Q1, Q3, IIQ, limite_inferior, limite_superior = get_stats(dataset['Valor'])
select = (dataset['Valor'] >= limite_inferior) & (dataset['Valor'] <= limite_superior)
dataset_without_outliers = dataset[select]

# dataset_without_outliers['Valor'].plot(kind='box')
# plt.show()
# dataset['Valor'].plot(kind='hist', title='Antes')
# plt.show()
# dataset_without_outliers['Valor'].plot(kind='hist', title='Depois')
# plt.show()

# Removendo outliers por grupo
group_tipo_valor = dataset.groupby('Tipo')['Valor']
Q1, Q3, IIQ, limite_inferior, limite_superior = get_stats(group_tipo_valor)
dataset_new = pd.DataFrame()

for tipo in group_tipo_valor.groups.keys():
    equals_tipo = dataset['Tipo'] == tipo
    inside_limit = (dataset['Valor'] >= limite_inferior[tipo]) & (dataset['Valor'] <= limite_superior[tipo])
    select = equals_tipo & inside_limit

    dataset_new = pd.concat([dataset_new, dataset[select]])

# dataset.boxplot(['Valor'], by=['Tipo'])
# plt.show()
# dataset_new.boxplot(['Valor'], by=['Tipo'])
# plt.show()

dataset_new.to_csv('./data/aluguel_residencial_sem_outliers.csv', sep=';', index=False)