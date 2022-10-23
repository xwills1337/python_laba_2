import pandas as pd
import datetime
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

name1 = '../program 1/X.csv'
name2 = '../program 1/Y.csv'
valid_date=datetime.date(2008, 1, 10)
invalid_date=datetime.date(2008, 1, 9)
print(get_data_x_y(name1,name2,valid_date))
print(get_data_x_y(name1,name2,invalid_date))