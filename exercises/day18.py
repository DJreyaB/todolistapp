# goal is to add an exit button and make theme black
import PySimpleGUI as sg

sg.theme("Black")

label1 = sg.Text("Enter feet:")
input1 = sg.InputText()
label2 = sg.Text("Enter inches:")
input2 = sg.InputText()
convert_btn = sg.Button("Convert")
exit_btn = sg.Button("Exit")
results = sg.Text('', key='meter')

layout = [[label1, input1],[label2, input2],[convert_btn, exit_btn, results]]

window = sg.Window('Converter', layout)

while True:
    events, values = window.read()
    print(events, values)
    match events:
        case 'Convert':
        #get feet and multiply by 12 then add inches answer and divide by 39.37
            inches_total = (float(values[0]) * 12) + float(values[1])
            print(inches_total)
            result = inches_total / 39.37
            print(result)
            window['meter'].update(value=f"{result} m")

            # layout = [[label1,input1],[label2, input2],[convert_btn]]
        case sg.WIN_CLOSED | 'Exit':
            break

window.close()

