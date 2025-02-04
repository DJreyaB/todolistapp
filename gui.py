import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input = sg.InputText(tooltip="Enter todo here")
add_button = sg.Button("Add")

layout = [[label],
          [input, add_button]]

window = sg.Window("My Todo App", layout)

window.read()
print("Hello")
window.close()