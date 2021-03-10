import os.path


class Las:
    list_LAS_to_analyze = []

    def __init__(self, file_name, folder_PSL):
        self.file_name = file_name
        self.folder_PSL = folder_PSL
        self.path_and_name = ""

        self.get_path_and_name_list()
        self.analisis_prueba()

    def get_path_and_name_list(self):
        for f in self.file_name:
            arch = str(os.path.join(self.folder_PSL, f))
            self.list_LAS_to_analyze.append(arch)

    def analisis_prueba(self):
        for p in self.list_LAS_to_analyze:
            with open(p, 'r') as file:
                for line in file:
                    if line.split()[0] == "CWN" or \
                            line.split()[0] == "STRT.M" or \
                            line.split()[0] == "STOP.M":
                        print(line)
