import PySimpleGUI as sg

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
select_files_btn = sg.FileBrowse("Choose")

label2 = sg.Text("Select folder for zip file destination")
input2 = sg.Input()
select_folder_btn = sg.FolderBrowse("Choose")

compress_btn = sg.Button("Compress")

layout = [[label1, input1, select_files_btn],
          [label2, input2, select_folder_btn],
          [compress_btn]]

window = sg.Window('File Zipper', layout)
while True:
    events, values = window.read()


window.close()

