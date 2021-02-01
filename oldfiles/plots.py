import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def rel_histogram():
    """Makes a relative histogram of a chosen variable"""
    np.random.seed(19680801)
    mu = -1
    sigma = 1.5
    n_bins = 8
    x = np.random.normal(mu, sigma, size=100)

    fig, ax = plt.subplots(figsize=(8, 4))

    # plot the cumulative histogram
    n, bins, patches = ax.hist(x, n_bins, density=True, histtype='step',
                               cumulative=True, label='Empirical')

    # Add a line showing the expected distribution.
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
    y = y.cumsum()
    y /= y[-1]

    ax.plot(bins, y, 'k--', linewidth=1.5, label='Theoretical')

    # tidy up the figure
    ax.grid(True)
    ax.legend(loc='right')
    ax.set_title('Cumulative step of variable')
    ax.set_xlabel('variable')
    ax.set_ylabel('Frequency')
    return fig


def circle_plt():
    layout = [[sg.Text("Finding out the chance for the values of", size=(31, 1), font=("Helvetica", 21)),
               sg.InputCombo(('value1', 'value2'), size=(10, 1))],
              [sg.Text("Binary elements to implemented:", size=(28, 1)),
               sg.Text("Non-binary elements to implemented:", size=(30, 1))],
              [sg.Listbox(values=('a', 'b', 'c', 'd', 'e'), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE,
                          visible=True, size=(30, 5)),
               sg.Listbox(values=('a', 'b', 'c', 'd', 'e'), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE,
                          visible=True, size=(30, 5))],
              [sg.Button('finalize decision', size=(27, 1)),
               sg.Button('finalize decision', size=(27, 1))],
              [sg.Text('Visualization of the chance:')],
              [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400),
                        background_color='white', key='graph')],
              [sg.T('Change circle color to:'), sg.Button('Firebrick'), sg.Button('Darkorange'), sg.Button('gold')]]

    window = sg.Window('Attribute exploration', layout, size=(700, 700))
    window.Finalize()

    graph = window['graph']
    circle = graph.DrawCircle((200, 200), 50, fill_color='teal', line_color='white')
    point = graph.DrawPoint((200, 200), 10, color='cadetblue')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event is 'Firebrick':
            graph.TKCanvas.itemconfig(circle, fill="Firebrick")
        elif event is 'Darkorange':
            graph.TKCanvas.itemconfig(circle, fill="Darkorange")
        elif event is 'gold':
            graph.TKCanvas.itemconfig(circle, fill="Gold")


def hist_plt():
    rel_histogram()

    matplotlib.use("TkAgg")

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
        return figure_canvas_agg

    layout = [[sg.Text("Finding out the chance for the values of", size=(31, 1), font=("Helvetica", 21)),
               sg.InputCombo(('value1', 'value2'), size=(10, 1))],
              [sg.Text("Binary elements to implemented:", size=(28, 1)),
               sg.Text("Non-binary elements to implemented:", size=(30, 1))],
              [sg.Listbox(values=('a', 'b', 'c', 'd', 'e'), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE,
                          visible=True, size=(30, 5)),
               sg.Listbox(values=('a', 'b', 'c', 'd', 'e'), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE,
                          visible=True, size=(30, 5))],
              [sg.Button('finalize decision', size=(27, 1)),
               sg.Button('finalize decision', size=(27, 1))],
              [sg.Text('Visualization of the chance:')],
              [sg.Canvas(key="-CANVAS-")]]
    window = sg.Window(
        "Matplotlib Single Graph",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center",
        font="Helvetica 18",
    )

    draw_figure(window["-CANVAS-"].TKCanvas, rel_histogram())
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close()



