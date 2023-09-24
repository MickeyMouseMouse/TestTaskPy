from Model import Model
from View import View
from pathlib import Path
from PyQt6.QtCore import QThread


class Controller:
    def __init__(self):
        self.working_dir = Path()  # current directory
        self.file_type = ""
        self.view = View(self)
        self.view.show()

    def getWorkingDir(self):
        return str(self.working_dir.resolve())

    def setWorkingDir(self, working_dir: str):
        path = Path(working_dir)
        if not path.is_dir():
            return False
        self.working_dir = path
        return True

    def start(self):
        self.thread = QThread()
        self.model = Model(self.working_dir, self.view.ui_main_window.comboBox.currentText())
        self.model.moveToThread(self.thread)

        self.thread.started.connect(self.model.run)
        self.thread.finished.connect(self.thread.deleteLater)

        self.model.started.connect(self.setTotalFiles)
        self.model.progress.connect(self.updateProgress)
        self.model.finished.connect(self.reset)

        self.thread.start()

    def setTotalFiles(self, amount):
        if amount:
            self.view.ui_main_window.label_status.setText(f"Загружено 0 из {amount} файлов")
            self.view.ui_main_window.progressBar.reset()
            self.view.ui_main_window.progressBar.setMaximum(amount)
        else:
            self.view.showMessage("Сообщение", "Файлы для обработки не найдены")

    def updateProgress(self, number):
        self.view.ui_main_window.label_status.setText(
            f"Загружено {number} из {self.view.ui_main_window.progressBar.maximum()} файлов"
        )
        self.view.ui_main_window.progressBar.setValue(number)

    def reset(self):
        self.thread.quit()
        self.model.deleteLater()
        self.view.ui_main_window.label_status.setText("Выберите директорию, тип и нажмите Запуск")
