import pandas as pd
df = pd.read_csv('../data.csv', sep=';', encoding='cp1251')

mas=list(range(7))
max=df.shape[0]
while (max>7):

    lf = df.loc[mas[0]:mas[-1]]

    data=lf['Дата'].iloc[0].replace('.', '')+"_"+lf['Дата'].iloc[lf.shape[0]-1].replace('.', '')
    lf.to_csv(data + ".csv", sep=';', encoding='cp1251', index=False)

    mas = [i + 7 for i in mas]
    max=max-7
if (max>0):
    lf=df.loc[df.shape[0]-max:df.shape[0]-1]
    data = lf['Дата'].iloc[0].replace('.', '') + "_" + lf['Дата'].iloc[lf.shape[0] - 1].replace('.', '')
    lf.to_csv(data + ".csv", sep=';', encoding='cp1251', index=False)
