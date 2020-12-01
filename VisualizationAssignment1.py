# =================================================================================================
# Name        : VisualizationAssignment1.py
# Author      : Fleur Ensink op Kemna, Job van Kempen, Ruben Kole, Gijs Thissen, and Michon Zeegers
# Version     :
# Copyright   : Your copyright notice
# Description : Group Assignment 1
# =================================================================================================

import pandas as pd

df = pd.read_excel(r'dataset.xlsx')

def parsing_function(row, column):
    """Take the value of a chosen cell"""
    return df.iloc[row, column]

def give_ages():
    """Returns the column age quantiles and age quantile frequencies"""
    ages = []
    new_dict = {}
    for i in df.iloc[:, 1]:
        ages.append(i)
    for i in range(20):
        number = ages.count(i)
        new_dict[i] = number
    """  
    Prints the top 10 age quantiles:
    sorted_dict = sorted(new_dict.items(), key=lambda item: item[1],reverse=True)

    for i in sorted_dict[0:10]:
        print(i[0], i[1])
    """
    return ages, new_dict

def missing_columns(row):
    """Returns the amount of empty columns in a given row."""
    return df.iloc[row].isnull().sum()

def missing_rows(column):
    """Returns the amount of empty rows in a given column."""
    return df.iloc[:,column].isnull().sum()

if __name__ == '__main__':
    parsing_function(6,6)
    give_ages()
    missing_columns(5)
    missing_rows(8)
