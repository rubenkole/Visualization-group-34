import os
import preprocessing as ppc
import pandas as pd
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3
import webbrowser
import numpy as np


if __name__ == '__main__':

    #df = pd.read_excel("dataset/dataset.xlsx")

    # df = pd.read_excel("dataset/Quantitative.xlsx")
    # quantitative_columns = df.columns.to_list()
    # edited_quantitative_columns = quantitative_columns[1:]
    #
    # def Converter(cols):
    #     first_list = []
    #     second_list = []
    #     for n, j in enumerate(cols):
    #         first_list.append(cols[n])
    #         _ = j.replace(" ","")
    #         second_list.append(_)
    #
    #     result_list = dict(zip(first_list,second_list))
    #     return result_list
    #
    # cols = Converter(edited_quantitative_columns)
    #

    # notsorted.pkl openen:
    #
    # file = open('notsorted.pkl', 'rb')
    # data = pickle.load(file)
    # IMPORTANT: AGEQUANTILE MANUALLY EDDITED, SORT BY FIRST COLUMN AND IMPUTED 0 IN NAN
    # data.to_excel("dataset/agequantile.xlsx")

    # Scatter.py:
    # The Quantitative, old system, this is more reactive to changes in the dataset
    # df = pd.read_excel("dataset/Quantitative.xlsx")
    #
    # quantitative_columns = df.columns.to_list()
    # options = quantitative_columns[1:]

    # ppc.create_quantitative_xlsx(df)
    # ppc.create_categorical_xlsx(df)


    # data = pd.read_excel("dataset/wards.xlsx",header=None)
    # improved = pd.read_excel("dataset/improved.xlsx")
    #
    #
    # data_as_numpy = np.asarray(data)
    # outputa = np.sum(data_as_numpy, 1, keepdims=True)
    #
    # ds = pd.DataFrame(outputa)
    # improved.insert(4, "Ward",outputa)
    # improved.to_excel("dataset/improved.xlsx")

    #my_dict = {}

    # Load in the improved dataset
    # dataset = pd.read_excel("dataset/improved.xlsx")

    # Sort the dataset into two datasets: Positive and Negative
    # positive_dataset = dataset[dataset['SARS-Cov-2 exam result'] == 'positive']
    #
    # positive_source = ColumnDataSource(
    #     data=dict(x=[], y=[], hematocrit=[], age_quantile=[]))
    #
    # positive_source.data = dict(
    #     x=positive_dataset["Hemoglobin"],
    #     y=positive_dataset["Hemoglobin"],
    #     hematocrit=positive_dataset["Ward"],
    #     age_quantile=positive_dataset["Patient age quantile"]
    # )
    #
    # testing = {0:"Hemoglobin"}
    # print(len(testing))
    # my_input = input(">>>")
    # testing[0] = my_input
    # print(list(testing.values())[0])

    # my_list = [1,2,3,4]
    # jochem = dict(my_list)
    # print(jochem)

    webbrowser.open("http://localhost:5006/app_dir")
    os.system("bokeh serve app_dir/properboxplot.py app_dir\scatter.py app_dir\sagequantile.py app_dir")

    #
    #
    # catList = ['negative','positive']
    # for cat in catList:
    #     catList.append(cat)
    #     print(cat)


 # jochem = pd.read_excel("dataset/Map1.xlsx",header=None)
    # print(jochem.shape)
    # data = [{'group':'negative','score': 1},
    #         {'group':'positive','score': 1}]
    #
    # # Creates padas DataFrame by passing
    # # Lists of dictionaries and row index.
    # df = pd.DataFrame(data, index=['negative', 'positive'])
    # jochem = df.to_string(index=False)
    # print(jochem)
    # webbrowser.open("http://localhost:5006/boxplot")
    # os.system("bokeh serve app_dir/boxplot.py")
    # webbrowser.open("http://localhost:5006/properboxplot")
    # os.system("bokeh serve app_dir/properboxplot.py")

    # webbrowser.open("http://localhost:5006/main")
    # os.system("bokeh serve app_dir/main.py")


