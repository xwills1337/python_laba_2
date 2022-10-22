import csv
import pandas as pd
df = pd.read_csv('../data.csv', sep=';', encoding='cp1251')
print(df.shape[0])

