import NotepadModel


class Controller:
    def __init__(self):
        self.notepadModel = NotepadModel.Model()

    def save_file(self, msg, url):
        self.notepadModel.save_file(msg, url)

    def save_as(self, msg, url):
        self.notepadModel.save_as(msg, url)

    def read_file(self, url):
        self.msg1, self.base = self.notepadModel.read_file(url)
        return self.msg1, self.base

    def saysomeThing(self):
        self.takeAudio=self.notepadModel.takeQuery()
        return self.takeAudio

