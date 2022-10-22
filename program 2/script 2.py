import csv
import pandas as pd

df = pd.read_csv('../data.csv', sep=';', encoding='cp1251')
first_data=int(df['Дата'][0][0]+df['Дата'][0][1]+df['Дата'][0][2]+df['Дата'][0][3])
last_data=int(df['Дата'][df.shape[0]-1][0]+df['Дата'][df.shape[0]-1][1]+df['Дата'][df.shape[0]-1][2]\
                                                                       +df['Дата'][df.shape[0]-1][3])
df.insert(0, "data_2", 0)
for i in range(df.shape[0]):
    str_1=df['Дата'][i]
    df.loc[i,'data_2']=int(str_1[0]+str_1[1]+str_1[2]+str_1[3])

for first_data in range(first_data, last_data+1):

    lf=df[df['data_2']==first_data]
    print(lf)
