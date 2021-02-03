import os
import preprocessing as ppc
import pandas as pd
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3
import webbrowser

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
    # file = open('notsorted.pkl', 'rb')
    # data = pickle.load(file)
    # IMPORTANT: AGEQUANTILE MANUALLY EDDITED, SORT BY FIRST COLUMN AND IMPUTED 0 IN NAN
    # data.to_excel("dataset/agequantile.xlsx")

    # ppc.create_quantitative_xlsx(df)
    # ppc.create_categorical_xlsx(df)



    os.system("bokeh serve app_dir\scatter.py app_dir\sagequantile.py app_dir")
    #os.system("bokeh serve testing.py --show")



