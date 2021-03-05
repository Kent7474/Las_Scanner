class Las:

    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def __scan(lasFile):
        """ LAS file scanner, searching for Uwi, name, logs and depth """
        print(lasFile)

    def scanning(self):
        self.__scan(self.file_name)
