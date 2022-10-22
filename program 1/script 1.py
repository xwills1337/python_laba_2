import csv
import pandas as pd
df = pd.read_csv('../data.csv', sep=';', encoding='cp1251')
df['Дата'].to_csv('X.csv', sep=';', encoding='cp1251', index=False)
del df['Дата']
df.to_csv('Y.csv', sep=';', encoding='cp1251', index=False)