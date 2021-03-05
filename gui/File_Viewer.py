import PySimpleGUI as sg
import os.path


class LasViewer:
    moutList = []
    listSelectLas = ""

    def __init__(self):

        self.file_list_column = [
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

        self.las_viewer_column = [
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

        self.layout = [
            [
                sg.Column(self.file_list_column),
                sg.VSeparator(),
                sg.Column(self.las_viewer_column)
            ]
        ]

        self.window = sg.Window("LAS Viewer", self.layout)

        # MAIN WHILE WINDOW
        while True:
            self.event, self.values = self.window.read()
            print(self.event)
            if self.event == "Exit" or self.event == sg.WIN_CLOSED:
                break

            self.__folder(self.event, self.values, self.window)

            if self.event == "Clear":
                self.__clear(self.window, self.listSelectLas)
                self.listSelectLas = ""

            self.__select_item_from_list(self.event, self.values, self.window, self.moutList, self.listSelectLas)

    # SELECT FOLDER AND LIST THE FILE NAMES FUNCTION
    @staticmethod
    def __folder(event, values, window):
        """SELECT FOLDER AND LIST THE FILE NAMES FUNCTION"""
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

    # CLEAR FILE LIST FUNCTION
    @staticmethod
    def __clear(window, listSelectLas):
        """CLEAR FILE LIST FUNCTION"""
        window["-MOUT-"].update("")
        print(listSelectLas)

    @staticmethod
    def __select_item_from_list(event, values, window, moutList, listSelectLas):
        print(listSelectLas)
        if event == "-FILE LIST-":
            try:
                fileListed = values["-FILE LIST-"][0]
                moutList.append(fileListed)
                print(fileListed)
                listSelectLas = ""
                for f in moutList:
                    listSelectLas += f + "\n"
                window["-MOUT-"].Update(listSelectLas)
            except:
                print("Please select File Folder containing *.las")


las = LasViewer()