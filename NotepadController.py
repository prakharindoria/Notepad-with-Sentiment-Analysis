import NotepadModel

class Controller:
    #Instanciate Model
    def __init__(self):
        self.model = NotepadModel.Model()
        print(self.__dict__)

    #Call savefile of Model
    def save_file(self, msz, url):
        self.model.save_file(msz, url)

    # Call saveAs of Model
    def save_as(self, msz, url):
        self.model.save_as(msz, url)

    # Call readFile of Model
    def read_file(self, path):
        self.file_content, self.file = self.model.read_file(path)
        return self.file_content, self.file

    # Call takeQuery of Model for Voice Input
    def saySomething(self):
        self.takeAudio=self.model.takeQuery()
        return self.takeAudio