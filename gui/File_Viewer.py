import PySimpleGUI as sg
import os.path


class LasViewer:
    list_file_selected = []
    folder_PSL = ""

    def __init__(self):

        self.file_list_column = [
            [
                sg.Text("File Folder"),
                sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Listbox(values=[], enable_events=True, size=(60, 30), key="-FILE LIST-"),
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
            [sg.Listbox(values=[], enable_events=True, size=(60, 20), key="-LIST OUT-")],
            [sg.HSeparator()],
            [
                sg.Button("Clear"),
                sg.Button("List"),
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

        # ----------------------------------------------------------------
        # MAIN WHILE WINDOW
        # -----------------------------------------------------------------
        while True:
            self.event, self.values = self.window.read()
            print(self.event)

            if self.event == "Exit" or self.event == sg.WIN_CLOSED:
                break

            self.__folder(self.event, self.values, self.window)
            if self.event == "Clear":
                self.__clear(self.window, self.event)
                self.list_file_selected = []
            self.__select_item_from_list(self.event, self.values, self.window, self.list_file_selected)
            self.__delete_item_from_list(self.event, self.values, self.window, self.list_file_selected)
            self.__list_button(self.event, self.list_file_selected, self.folder_PSL)

        self.window.close()

    # SELECT FOLDER AND LIST THE FILE NAMES FUNCTION
    def __folder(self, event, values, window):
        """SELECT FOLDER AND LIST THE FILE NAMES FUNCTION"""
        if event == "-FOLDER-":
            self.folder_PSL = values["-FOLDER-"]
            print(self.folder_PSL)
            try:
                file_list = os.listdir(self.folder_PSL)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(self.folder_PSL, f))
                   and ".las" in f.lower()
            ]
            fnames.sort()
            window["-FILE LIST-"].update(fnames)

    # CLEAR FILE LIST FUNCTION
    @staticmethod
    def __clear(window, event):
        """CLEAR FILE LIST FUNCTION"""
        window["-LIST OUT-"].update("")

    @staticmethod
    def __select_item_from_list(event, values, window, list_file_selected):
        """SELECT A .LAS FILE AND ADD TO THE LIST THAT WILL USE TO READ"""
        if event == "-FILE LIST-":
            try:
                fileListed = values["-FILE LIST-"][0]
                if fileListed not in list_file_selected:
                    list_file_selected.append(fileListed)
                    print(fileListed)
                list_file_selected.sort()
                window["-LIST OUT-"].Update(list_file_selected)
            except:
                print("Please select File Folder containing *.las")

    def __delete_item_from_list(self, event, values, window, list_file_selected):
        """SELECT A FILE TO DELETE"""
        if event == "-LIST OUT-":
            print(event)
            try:
                to_delete = values["-LIST OUT-"][0]
                list_file_selected.remove(to_delete)
                list_file_selected.sort()
                window["-LIST OUT-"].update(list_file_selected)
            except:
                print("Delete Failed")

    @staticmethod
    def __list_button(event, moutList, folder_PSL):
        """NEW SCAN WINDOW class: LasScanned"""
        if event == "List":
            print(moutList)
            LasScanned(moutList,folder_PSL)


class LasScanned:
    """OPEN NEW WINDOW"""

    saved_las = []

    def __init__(self, list_file_selected, folder_PSL):

        self.folder_PSL = folder_PSL
        self.list_file_selected = list_file_selected
        self.out_list = self.show_files(list_file_selected)

        self.file_scanned = [
            [
                sg.Multiline(size=(60, 30), enable_events=True, key="-RESULT-"),
            ],
            [
                sg.Button("Exit", size=(5, 1)),
                sg.Button("SCAN", size=(7, 1))
            ]
        ]

        self.work_column = [
            [sg.Listbox(values=list_file_selected, enable_events=True, size=(60, 25), key="-FILE LIST2-")],
            [sg.In(size=(25, 1), enable_events=True, key="-SAVE IN-")],
            [sg.Button("Save .las", size=(8, 1)), sg.Button("View List Saved", size=(12, 1))]
        ]

        self.layout = [
            [
                sg.Column(self.file_scanned),
                sg.VSeparator(),
                sg.Column(self.work_column)
            ]
        ]

        self.window_scanned = sg.Window("RESULTS", self.layout)

        # ----------------------------------------------------------------
        # MAIN WHILE WINDOW
        # -----------------------------------------------------------------

        while True:
            self.event, self.value = self.window_scanned.read()
            print("-------------------- window 2 --------------------")
            print(self.event)
            print(self.value)

            if self.event == "Exit" or self.event == sg.WIN_CLOSED:
                self.window_scanned.close()
                break

            self.__scan_las_in_FILE_LIST2(self.event, self.window_scanned, self.list_file_selected)
            self.__fill_save_las(self.event, self.value, self.window_scanned)
            self.__view_list_saved(self.event, self.saved_las)

    def __scan_las_in_FILE_LIST2(self, event, window, list_file_selected):
        if event == "SCAN":
            print("lista 1")
            print(list_file_selected)

            window["-RESULT-"].update(list_file_selected)
            print("lista 2")
            print(list_file_selected)

    def show_files(self, list_file_selected):
        out = ""
        for f in list_file_selected:
            out += f + "\n"
        return out

    def __fill_save_las(self, event, values, window):
        if event == "-FILE LIST2-":
            try:
                arch_name = values["-FILE LIST2-"][0]
                print(arch_name)
                window["-SAVE IN-"].update(arch_name)
            except:
                print("FILE LIST2 empty")

        if event == "Save .las":
            arch2save = values["-SAVE IN-"]
            list_arch_name = str(os.path.join(self.folder_PSL, arch2save))
            print(list_arch_name)

            if arch2save != "" and list_arch_name not in self.saved_las:
                self.saved_las.append(list_arch_name)

            print(self.saved_las)

    def __view_list_saved(self, event, saved_las):
        pass


lasViewerSurface = LasViewer()