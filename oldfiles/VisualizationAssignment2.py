# =================================================================================================
# Name        : VisualizationAssignment2.py
# Author      : Fleur Ensink op Kemna, Job van Kempen, Ruben Kole, Gijs Thissen, and Michon Zeegers
# Version     :
# Copyright   : Your copyright notice
# Description : Group Assignment 2
# =================================================================================================

#This file only works with an edited dataset, might change that
#Imputating medical data with generated data is a bad idea
#However, this was for an assignment

import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
import csv

df = pd.read_excel(r'dataset.xlsx')


def parsing_function(row, column):
    """Take the value of a chosen cell"""
    return df.iloc[row, column]

def nested_list(df):
    """Creates a nested list from the dataset denoted as df"""
    nan = np.nan
    job = []
    for i in range(df.shape[0]):
        gijs = []
        for j in range(1,df.shape[1]):
            a = df.iloc[i,j]
            if a == 'negative':
                a = 0
            elif a == 'positive':
                a = 1
            elif a == 'not_detected':
                a = 0
            elif a == 'detected':
                a = 1
            elif a == '<1000':
                a = 0
            elif a == 'Não Realizado':
                a = nan
            elif a == 'not_done':
                a = nan
            gijs.append(a)
        job.append(gijs)
    return job

def KNNMeuk(df):
    """Applies KNN on the dataset using the nested list function"""
    nan = np.nan
    x = nested_list(df)
    imputer = KNNImputer(n_neighbors=2,weights="uniform")
    return imputer.fit_transform(x)

def nestedlistexporter(x):
    """Writes a nested list to a csv file"""
    file_name = "improveddataset.csv"
    with open(file_name, 'w') as f:
        fc = csv.writer(f, lineterminator='\n')
        fc.writerows(x)

if __name__ == '__main__':
    a = KNNMeuk(df)
    nestedlistexporter(a)


