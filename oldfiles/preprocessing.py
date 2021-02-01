# =================================================================================================
# Name        : preprocessing.py
# Author      : Gijs Thissen
# Version     : 2.0
# Description : Preprocessing of the dataset for the course Visualisation 2020-2021 (Group 34)
# =================================================================================================
# Libraries
import pandas as pd

def dropuseless(df):
    """Drops the rows with minimal values"""
    fa = df.iloc[df["Red blood Cells"].dropna().index, :]
    return fa

def drop_empty(df):
    """Drops the empty columns"""
    af = dropuseless(df)

    empty_cols = [col for col in af.columns if af[col].isnull().all()]
    post_drop = af.drop(empty_cols, axis=1)
    return post_drop

def create_quantitative_xlsx(data_frame):
    """Creates a separate file for Quantitative data"""
    df = drop_empty(data_frame)

    cols = df.columns  # total columns
    num_cols = df._get_numeric_data().columns
    return_list = list(set(cols) - set(num_cols))  #return_list is the list of columns with the ones with numerical data

    # In case you consider pH and Leukocytes to be Quantitative uncomment the following 2 lines:
    # return_list.remove('Urine - pH')
    # return_list.remove('Urine - Leukocytes')

    numerical_set = df.drop(return_list,axis=1)
    numerical_set.to_excel("Quantitative.xlsx")

def create_categorical_xlsx(data_frame):
    """Creates a separate file for Categorical data"""
    df = drop_empty(data_frame)

    num_cols = list(df._get_numeric_data().columns)

    # In case you consider pH and Leukocytes to be Quantitative uncomment the following 2 lines:
    # exemption_list = ['Urine - pH','Urine - Leukocytes']
    # num_cols += exemption_list

    categorical_set = df.drop(num_cols,axis=1)
    categorical_set.to_excel("Categorical.xlsx")

if __name__ == '__main__':
    af = pd.read_excel("dataset.xlsx")

    create_quantitative_xlsx(af)
    create_categorical_xlsx(af)

