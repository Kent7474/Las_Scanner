import os.path


class Las:
    list_LAS_to_analyze = []


    def __init__(self, file_name, folder_PSL):
        self.file_name = file_name
        self.folder_PSL = folder_PSL
        self.path_and_name = ""
        self.result_from_scan = ""

        self.get_path_and_name_list()
        # self.analyze_prueba()

    def get_path_and_name_list(self):
        for f in self.file_name:
            arch = str(os.path.join(self.folder_PSL, f))
            self.list_LAS_to_analyze.append(arch)
        print(self.list_LAS_to_analyze)

    def analyze_prueba(self):

        for p in self.list_LAS_to_analyze:
            start = None
            stop = None
            logs = []

            self.result_from_scan += self.file_name + "\n"
            arch = open(p, "r")

            line = arch.readline()
            while line.split() != [] and line != '':
                self.__depth(start, stop, line)

        return self.result_from_scan

    def __depth(self, start, stop, line):
        if line.split()[0] == 'STRT':
            start = line.split()[2]
            print(start)
        elif line.split()[0] == 'STRT.' or 'STRT.m' or 'STRT.M':
            start = line.split()[1]
            print(start)
