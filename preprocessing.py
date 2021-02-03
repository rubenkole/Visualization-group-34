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
    global fa
    fa = df.iloc[df["Red blood Cells"].dropna().index, :]
    return fa


def tresholdfunction(df, treshold):
    """Finds the treshold of the given value, a maximum of empty is inputted value"""
    train = dropuseless(df)
    a = train.isnull().sum() / len(train) * 100  # calculate amount empty
    variables = train.columns
    variable = []
    for i in range(0, 111):
        if a[i] <= treshold:  # if lower than the given threshold
            variable.append(variables[i])
    return variable


def find_empty(df):
    """Locates empty list of features and returns list"""
    temp1 = tresholdfunction(df, 99)
    temp2 = tresholdfunction(df, 100)
    resultinglist = list(set(temp2) - set(temp1))

    return resultinglist


def drop_empty(df):
    """Drops the empty columns"""
    af = dropuseless(df)

    empty_cols = find_empty(df)
    post_drop = af.drop(empty_cols, axis=1)

    # The doctors at the hospital decided to put a string in a pH-value column.
    # The following line removes "Não Realizado" from the column since it was causing issues
    # "Não Realizado" means "unfulfilled" or "unrealized" and was therefore replaced with an empty value.
    post_drop['Urine - pH'] = post_drop['Urine - pH'].replace(['Não Realizado'], '')

    return post_drop


def create_quantitative_xlsx(data_frame):
    """Creates a separate file for Quantitative data"""
    df = drop_empty(data_frame)

    cols = df.columns  # total columns
    num_cols = df._get_numeric_data().columns
    return_list = list(
        set(cols) - set(num_cols))  # return_list is the list of columns with the ones with numerical data

    # The drop function works in that it removes a given list.
    # Exemption list is a list of exemptions that will be added to the list of things that would be removed
    exemption_list = ["Patient age quantile", "Patient addmited to regular ward (1=yes, 0=no)",
                      "Patient addmited to semi-intensive unit (1=yes, 0=no)",
                      "Patient addmited to intensive care unit (1=yes, 0=no)"]
    # In case you consider pH and Leukocytes to be Quantitative uncomment the following 2 lines:
    # return_list.remove('Urine - pH')
    # return_list.remove('Urine - Leukocytes')
    return_list += exemption_list

    numerical_set = df.drop(return_list, axis=1)
    numerical_set.to_excel("dataset/Quantitative.xlsx")


def create_categorical_xlsx(data_frame):
    """Creates a separate file for Categorical data"""
    df = drop_empty(data_frame)

    num_cols = list(df._get_numeric_data().columns)

    #The drop function works in that it removes a given list.
    #Exemption list is a list of exemptions that will be removed from the list of things that would be removed
    exemption_list = ["Patient age quantile", "Patient addmited to regular ward (1=yes, 0=no)",
                      "Patient addmited to semi-intensive unit (1=yes, 0=no)",
                      "Patient addmited to intensive care unit (1=yes, 0=no)"]

    for i in exemption_list:
        num_cols.remove(i)

    # In case you consider pH and Leukocytes to be Quantitative uncomment the following 2 lines:
    # exemption_list = ['Urine - pH','Urine - Leukocytes']
    # num_cols += exemption_list

    #This column however needs to be removed
    num_cols += ["Patient ID"]

    #Drop the columns as specified in num_cols
    categorical_set = df.drop(num_cols, axis=1)
    categorical_set.to_excel("dataset/Categorical.xlsx")


if __name__ == '__main__':
    af = pd.read_excel("dataset/dataset.xlsx")

    df = drop_empty(af)
    df.to_excel("dataset/improved.xlsx")
    # create_quantitative_xlsx(af)
    # create_categorical_xlsx(af)
