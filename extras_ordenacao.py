import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

df = pd.DataFrame(data, index=list('321'), columns=list('zyx'))

print('Ordenando pelo índice:\n')
df.sort_index(inplace=True)
print(df)

print('\nOrdenando pelo nome das colunas:\n')
df.sort_index(inplace=True, axis=1)
print(df)

print('\nOrdenando pelo valor das colunas:\n')
df.sort_values(inplace=True, by=['x', 'y'])
print(df)

print('\nOrdenando pelo valor das linhas:\n')
df.sort_values(inplace=True, by=['3'], axis=1)
print(df)
