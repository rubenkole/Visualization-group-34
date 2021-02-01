import os
import preprocessing as ppc
import pandas as pd


if __name__ == '__main__':
    df = pd.read_excel("dataset/dataset.xlsx")

    ppc.create_quantitative_xlsx(df)
    ppc.create_categorical_xlsx(df)

    os.system("bokeh serve app_dir\scatter.py app_dir\sagequantile.py app_dir --show")
