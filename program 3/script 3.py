import pandas as pd
def create_file(df: pd.DataFrame, mas: list[int]) -> None:
    """ Creates a .csv file with single week data
    Args:
        df (pd.DataFrame): this DataFrame
        mas (list[int]): List of indices for which data is selected
    Returns:
        None
    """
    lf = df.loc[mas[0]:mas[-1]]
    data = lf['Дата'].iloc[0].replace('.', '') + "_" + lf['Дата'].iloc[lf.shape[0] - 1].replace('.', '')
    lf.to_csv(data + ".csv", sep=';', encoding='cp1251', index=False)

if __name__ == "__main__":

    df = pd.read_csv('../data.csv', sep=';', encoding='cp1251')
    mas = list(range(7))
    max = df.shape[0]

    while (max > 0):
        create_file(df, mas)
        mas = [i + 7 for i in mas]
        max = max-7

