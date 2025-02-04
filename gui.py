import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input = sg.InputText(tooltip="Enter todo here", key="todo")
add_button = sg.Button("Add") #add an option that accepts enter
exit_button = sg.Button("Exit")

layout = [[label],
          [input, add_button],
          [exit_button]]

window = sg.Window("My Todo App", layout,
                   font=("Helvetica", 16))
while True:
    events, values = window.read()
    print(events, values)

    match events:
        case "Add":
            #adds todo to running list then places them in the file
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            
            functions.write_todos(todos)
        case "Exit" | sg.WIN_CLOSED:
            break
window.close()