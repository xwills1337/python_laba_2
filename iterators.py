import pandas as pd
import datetime
import os

class DateIterator:
    def __init__(self):

        self.counter = 0
        self.df =pd.read_csv( 'data.csv', sep=';', encoding='cp1251')
    def __next__(self) -> tuple:
        if self.counter == self.df.shape[0]:
            return (self.df.loc[self.counter - 1][0], self.df.loc[self.counter - 1][1],self.df.loc[self.counter - 1][2],
                                                      self.df.loc[self.counter - 1][3], self.df.loc[self.counter - 1][4],
                                                      self.df.loc[self.counter - 1][5], self.df.loc[self.counter - 1][6])
        elif self.counter < self.df.shape[0]:
            self.counter += 1
            return (self.df.loc[self.counter - 1][0], self.df.loc[self.counter - 1][1], self.df.loc[self.counter - 1][2],
                                                      self.df.loc[self.counter - 1][3], self.df.loc[self.counter - 1][4],
                                                      self.df.loc[self.counter - 1][5], self.df.loc[self.counter - 1][6])

class DateIterator_X_Y:
    def __init__(self):

        self.counter = 0
        self.lf = pd.read_csv('program 1/X.csv', sep=';', encoding='cp1251')
        self.df = pd.read_csv('program 1/Y.csv', sep=';', encoding='cp1251')
    def __next__(self) -> tuple:
        if self.counter == self.df.shape[0]:
            return (self.lf.loc[self.counter - 1][0], self.df.loc[self.counter - 1][0], self.df.loc[self.counter - 1][1],
                                                      self.df.loc[self.counter - 1][2], self.df.loc[self.counter - 1][3],
                                                      self.df.loc[self.counter - 1][4], self.df.loc[self.counter - 1][5])
        elif self.counter < self.df.shape[0]:
            self.counter += 1
            return (self.lf.loc[self.counter - 1][0], self.df.loc[self.counter - 1][0], self.df.loc[self.counter - 1][1],
                                                      self.df.loc[self.counter - 1][2], self.df.loc[self.counter - 1][3],
                                                      self.df.loc[self.counter - 1][4], self.df.loc[self.counter - 1][5])

if __name__ == "__main__":
    obj = DateIterator_X_Y()
    while(True):
        print(next(obj))

