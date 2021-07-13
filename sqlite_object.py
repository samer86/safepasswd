# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:55:30 2021

@author: salem
"""
from IPython.display import display
import sqlite3
from sqlite3 import Error
import pandas as pd
import sys
'''CONNECT USING sqlite3 '''
# print("Opened database successfully")

# c = sqlite3.connect('class.db')


class database():
    __c = ''
    stmt = ''
    results = []
    columns = []
    __data = ''
    __tables = ''
    auto_print = True

    def __init__(self, db_name):
        self.__c = sqlite3.connect(db_name)
        self.tables

    @property
    def stmt(self):
        print(self.__query)
        return self.__query

    def query(self, stmt, **kwargs):
        self.__query = stmt
        try:
            if stmt.lower().strip()[0:6] == 'select':
                self.__data = pd.read_sql_query(stmt, self.__c, **kwargs)
                # print(self.__data)
            else:
                res = self.__c.execute(stmt)
                print('Query Successfully Finished!')
                self.__data = 'No Returned Data'
                if res.rowcount != -1:
                    print(f'Affected rows: {res.rowcount}')

        except:
            print(sys.exc_info()[1])

        finally:
            return self.__data

    @property
    def conn(self):
        return self.__c

    def data(self):
        return self.__data

    def commit(self):
        self.__c.commit()

    @property
    def tables(self):
        pass

    @tables.setter
    def tables(self, stmt):
        pass

    def save_history(self, stmt):
        pass

    def __setattr__(self, name, value):
        if name == "query":
            print(''' Protected Method! ''')

        else:
            super().__setattr__(name, value)


# db = database()


########## [####] ###########


class nc(database):

    __cmd_history = []
    saving_history = ''
    hi = 'Hello'

    def __init__(self):
        self.history = history()
        self.saving_history = input('yes/no : ')
        # print('Hello From class')

    def save_history(self, stmt):
        if self.saving_history == 'yes':
            temp = input('Please Enter CMD name: ')
            if temp != '':
                self.__cmd_history.append({"CMD_Name": temp, "CMD": stmt})

    @property
    def history(self):
        return pd.DataFrame.from_dict(self.__cmd_history)

    @history.setter
    def history(self):
        pass


def main():
    pass
    # db=nc()
    # newclass = nc()


if __name__ == "__main__":
    # main()
    db = nc()
