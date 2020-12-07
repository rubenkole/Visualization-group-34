
import PySimpleGUI as sg

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

circle_plt()