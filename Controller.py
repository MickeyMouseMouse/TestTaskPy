from View import View
from pathlib import Path


class Controller:
    def __init__(self, model):
        self.model = model
        self.view = View(self, self.model)
        self.view.show()

    def getWorkingDir(self):
        return str(self.model.working_dir.resolve())

    def setWorkingDir(self, working_dir: str):
        path = Path(working_dir)
        if not path.is_dir():
            return False
        self.model.setWorkingDir(path)
        return True

    def start(self):
        self.model.setFileType(self.view.ui_main_window.comboBox.currentText())
        self.model.handle()

