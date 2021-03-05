import PySimpleGUI as sg
import os.path


# las1 = Las("asdfasdf.las")
#
# las1.scanning()



def Surface():
    moutList = []

    file_list_column = [
        [
            sg.Text("File Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(values=[], enable_events=True, size=(50, 30), key="-FILE LIST-"),
        ],
        [
            sg.HSeparator()
        ],
        [
            sg.Button("Exit", size=(5, 1)),

        ]
    ]

    las_viewer_column = [
        [sg.Text("Choose a .las from list on left:")],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Multiline(size=(60, 30), key="-MOUT-")],
        [sg.HSeparator()],
        [
            sg.Button("Clear"),
            sg.Button("List"),
            sg.In(size=(25, 1), enable_events=True, key="-CUENCA-"),
        ],
    ]

    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeparator(),
            sg.Column(las_viewer_column)
        ]
    ]

    window = sg.Window("LAS Viewer", layout)

    while True:
        event, values = window.read()
        print(event)

        # EXIT
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        # SELECT FOLDER
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                   and ".las" in f.lower()
            ]
            fnames.sort()
            window["-FILE LIST-"].update(fnames)

        # SELECT AN ITEM IN FILE LIST
        if event == "-FILE LIST-":
            try:
                fileListed = values["-FILE LIST-"][0]
                print(fileListed)
                moutList.append(fileListed)
                lista = ""
                for f in moutList:
                    lista += f + "\n"
                window["-MOUT-"].update(lista)
            except:
                print("Please, select File Folder")

        if event == "Clear":
            lista = ""
            window["-MOUT-"].update(lista)
        # print(event)
        # print(values)
