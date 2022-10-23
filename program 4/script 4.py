import pandas as pd
import datetime
import os
def get_data_x_y(name_x: str, name_y: str, date: datetime.date) -> list[str] or None:
    df_x = pd.read_csv(name_x, sep=';', encoding='cp1251')
    df_y = pd.read_csv(name_y, sep=';', encoding='cp1251')
    index = -1
    for i in range(df_x.shape[0]):
        if (df_x['Дата'].iloc[i].replace('.', '')==str(date).replace('-', '')):
            index=i
            break
    if (index>=0):
        return df_y.iloc[index]
    return None
def get_data_year_or_month(name_y_or_m: str, date: datetime.date) -> list[str] or None:
    for root, dirs, files in os.walk(name_y_or_m):
        for file in files[0: -1: 1]:
            df=pd.read_csv(name_y_or_m+file, sep=';', encoding='cp1251')
            for i in range(df.shape[0]):
                if (df['Дата'].iloc[i].replace('-', '') == str(date).replace('-', '') or
                    df['Дата'].iloc[i].replace('.', '') == str(date).replace('-', '')):
                    return df.iloc[i]
    return None


name1 = '../program 1/X.csv'
name2 = '../program 1/Y.csv'
name3 = '../program 2/'
name4 = '../program 3/'
valid_date=datetime.date(2008, 1, 10)
invalid_date=datetime.date(2008, 1, 9)
#print(get_data_x_y(name1,name2,valid_date))
#print(get_data_x_y(name1,name2,invalid_date))
#print(get_data_year_or_month(name3, valid_date))
#print(get_data_year_or_month(name3, invalid_date))
#print(get_data_year_or_month(name4, valid_date))
#print(get_data_year_or_month(name4, invalid_date))