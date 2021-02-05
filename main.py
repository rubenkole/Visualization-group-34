import os
import webbrowser

if __name__ == '__main__':
    webbrowser.open("http://localhost:5006/quantitative")
    os.system("bokeh serve app_dir\quantitative.py app_dir\categorical.py")