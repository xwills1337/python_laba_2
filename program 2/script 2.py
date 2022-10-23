import pandas as pd

def create_data_2(df: pd.DataFrame) -> pd.DataFrame:
    """ Adds a new column of years to the DataFrame
    Args:
        df (pd.DataFrame): this DataFrame
    Returns:
        pd.DataFrame: DataFrame with new column
    """
    df['Дата'] = pd.to_datetime(df['Дата'], format="%Y.%m.%d")
    df['data_2'] = df['Дата'].dt.year
    df['Дата'] = df['Дата'].dt.date

    return df

def create_file(df: pd.DataFrame, year: int) -> None:
    """ Creates a .csv file with single year data
    Args:
        df (pd.DataFrame): this DataFrame
        year(int): Data is collected for this year
    Returns:
        None
    """
    lf = df[df['data_2'] == year]
    data = str(lf['Дата'].iloc[0]).replace('-', '') + "_" + str(lf['Дата'].iloc[lf.shape[0] - 1]).replace('-', '')
    del lf['data_2']
    lf.to_csv(data + ".csv", sep=';', encoding='cp1251', index=False)

if __name__ == "__main__":

    df = pd.read_csv('../data.csv', sep=';', encoding='cp1251')

    df = create_data_2(df)

    first_year=df['data_2'][0]
    last_year=df['data_2'][df.shape[0]-1]

    for first_year in range(first_year, last_year+1):
        create_file(df, first_year)

