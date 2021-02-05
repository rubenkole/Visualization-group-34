import os
import webbrowser

if __name__ == '__main__':
    webbrowser.open("http://localhost:5006/main")
    os.system("bokeh serve app_dir\scatter.py app_dir\main.py")

