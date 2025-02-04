import functions
import time
import PySimpleGUI as sg

sg.theme("DarkPurple1")

clock = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo here", key="todo")
add_btn = sg.Button("Add") #add an option that accepts enter
exit_btn = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos', enable_events=True,
                      size=[45,10])
edit_btn = sg.Button("Edit")
complete_btn = sg.Button("Complete")

layout = [[clock],
          [label],
          [input_box, add_btn],
          [list_box, edit_btn, complete_btn],
          [exit_btn]]

window = sg.Window("My Todo App", layout,
                   font=("Helvetica", 16))
while True:
    events, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(events, values)

    match events:
        case "Add":
            #adds todo to running list then places them in the file
            if len(values['todo'])>0:
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)             
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            else:
                sg.popup("Please enter a todo", font=("Helvetica", 16))
        case "Edit":
            try:
                #grab the selected row
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                #change selected row
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                #resave it to the txt file & update gui
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item", font=("Helvetica", 16))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                #grab the selected row
                todo_to_del = values['todos'][0]
                #change selected row
                todos = functions.get_todos()
                todos.remove(todo_to_del)
                #resave it to the txt file & update gui
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item", font=("Helvetica", 16))
        case "Exit" | sg.WIN_CLOSED:
            break
window.close()