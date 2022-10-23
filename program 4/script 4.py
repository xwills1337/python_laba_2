import pandas as pd
import datetime
import os

def get_data(name: str, date: datetime.date) -> list[str] or None:
    """ Find data for a specified date
    Args:
        name (str): file address
        date (datetime.date): this date
    Returns:
        list[str]: Found data
        None: Not found data
    """
    df = pd.read_csv(name, sep=';', encoding='cp1251')
    for i in range(df.shape[0]):
        if (df['Дата'].iloc[i].replace('.', '')==str(date).replace('-', '')):
            return df.iloc[i]
def get_data_x_y(name_x: str, name_y: str, date: datetime.date) -> list[str] or None:
    """ Find data for a specified date
     Args:
        name_x (str): date file address
        name_y (str): data file address
        date (datetime.date): this date
     Returns:
        list[str]: Found data
        None: Not found data
    """
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
    """ Find data for a specified date
    Args:
        name_y_or_m (str): file address
        date (datetime.date): this date
    Returns:
        list[str]: Found data
        None: Not found data
    """
    for root, dirs, files in os.walk(name_y_or_m):
        for file in files[0: -1: 1]:
            df=pd.read_csv(name_y_or_m+file, sep=';', encoding='cp1251')
            for i in range(df.shape[0]):
                if (df['Дата'].iloc[i].replace('-', '') == str(date).replace('-', '') or
                    df['Дата'].iloc[i].replace('.', '') == str(date).replace('-', '')):
                    return df.iloc[i]
    return None

def next_data() -> tuple[str]:
    """ generator function
    Args:

    Returns:
        tuple[str]: data
    """
    df = pd.read_csv('../data.csv', sep=';', encoding='cp1251')
    df.index = df['Дата']

    for data in df['Дата']:
        yield [data, df.loc[data][1], df.loc[data][2], df.loc[data][3], df.loc[data][4],
                                                       df.loc[data][5], df.loc[data][6]]
    while(True):
        yield [df.iloc[-1][0], df.iloc[-1][1], df.iloc[-1][2], df.iloc[-1][3], df.iloc[-1][4],
                                                               df.iloc[-1][5], df.iloc[-1][6]]

if __name__ == "__main__":

    name0 = '../data.csv'
    name1 = '../program 1/X.csv'
    name2 = '../program 1/Y.csv'
    name3 = '../program 2/'
    name4 = '../program 3/'
    valid_date=datetime.date(2008, 1, 10)
    invalid_date=datetime.date(2008, 1, 9)

    #n_d=next_data()
    #print(next(n_d))
    #print(next(n_d))
    #print(next(n_d))
    #print(next(n_d))

    #print(get_data(name0,valid_date))
    #print(get_data(name0,invalid_date))

    #print(get_data_x_y(name1,name2,valid_date))
    #print(get_data_x_y(name1,name2,invalid_date))

    #print(get_data_year_or_month(name3, valid_date))
    #print(get_data_year_or_month(name3, invalid_date))

    #print(get_data_year_or_month(name4, valid_date))
    #print(get_data_year_or_month(name4, invalid_date))