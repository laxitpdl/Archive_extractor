from zipextractor import extract_archive
import PySimpleGUI as sg

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select dest dir:")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key="folder")

button3 = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor",
                   layout = [[label1, input1, button1], 
                             [label2, input2, button2], 
                             [button3, output_label]])


while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed!")

window.close()

