import PySimpleGUI as sg
from plots import circle_plt, hist_plt
# menu
sg.theme('LightGreen3')

layout = [[sg.Text('Would you like to look at binary attributes?', justification='center')],
          [sg.B('yes', 'center', size=(5, 1)), sg.B('no', size=(5, 1))],
          [sg.Cancel()]]

window = sg.Window('Window Title', layout, element_justification='c')

event, values = window.read()
if event == 'Button':
    print('You will be redirected')
window.close()

# title binary
layout = [[sg.Text("Finding out the chance of")],
          [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1))]]

# Create the window
window = sg.Window("Attribute exploration", layout)
while True:
    event, values = window.read()
    # End program if user closes window or
    if event == sg.WIN_CLOSED:
        break
window.close()

# call the circle plot function
circle_plt()
hist_plt()

