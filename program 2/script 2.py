import pandas as pd
df = pd.read_csv('../data.csv', sep=';', encoding='cp1251')
df.insert(0, "data_2", 0)

for i in range(df.shape[0]):
    str_1=df['Дата'][i]
    df.loc[i,'data_2']=int(str_1[0]+str_1[1]+str_1[2]+str_1[3])

first_year=df['data_2'][0]
last_year=df['data_2'][df.shape[0]-1]

for first_year in range(first_year, last_year+1):
     lf=df[df['data_2']==first_year]
     data=lf['Дата'].iloc[0].replace('.', '')+"_"+lf['Дата'].iloc[lf.shape[0]-1].replace('.', '')
     del lf['data_2']
     lf.to_csv(data+".csv", sep=';', encoding='cp1251', index=False)
