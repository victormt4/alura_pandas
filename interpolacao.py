import pandas as pd

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)

df = pd.DataFrame(s, columns=['original'])

print('ffill - preenche o valor nulo atual com o último valor válido disponível:\n')
ff = pd.concat([
    df,
    pd.DataFrame(s.fillna(method='ffill'), columns=['new'])
], axis=1)
print(ff)

print('\nbfill - semelhante ao ffill, mas invertido:\n')
bf = pd.concat([
    df,
    pd.DataFrame(s.fillna(method='bfill'), columns=['new'])
], axis=1)
print(bf)

print('\npreenchendo os nulos com a media dos valores:\n')
bf = pd.concat([
    df,
    pd.DataFrame(s.fillna(s.mean()), columns=['new'])
], axis=1)
print(bf)

print('\npreenchendo os nulos com ffill e limit:\n')
bf = pd.concat([
    df,
    pd.DataFrame(s.fillna(method='ffill', limit=1), columns=['new'])
], axis=1)
print(bf)

print('\npreenchendo os nulos intercalando ffill e bfill:\n')
s = s.fillna(method='ffill', limit=1)
s = s.fillna(method='bfill', limit=1)

bf = pd.concat([
    df,
    pd.DataFrame(s, columns=['new'])
], axis=1)
print(bf)
