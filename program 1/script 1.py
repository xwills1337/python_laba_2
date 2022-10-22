import csv
import pandas as pd
df = pd.read_csv('../data.csv', sep=';', encoding='cp1251')
print(df)

df.to_csv('data2.csv', sep=';', encoding='cp1251', index=False)

df['Дата'].to_csv('X.csv', sep=';', encoding='cp1251', index=False)