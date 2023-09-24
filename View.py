from PyQt6.QtWidgets import QMainWindow, QDialog, QFileDialog, QMessageBox
from MainWindow import Ui_main_window
from SettingsDialog import Ui_settings_dialog


class View(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.ui_main_window = Ui_main_window()
        self.ui_main_window.setupUi(self)

        self.ui_main_window.menu.signal_click.connect(self.openSettings)

        self.ui_main_window.btn_start.clicked.connect(self.start)

    def openSettings(self):
        self.settings_dialog = SettingsDialog(self.controller)
        self.settings_dialog.show()

    def start(self):
        self.controller.start()

    def showMessage(self, title, text):
        dialog = QMessageBox(self)
        dialog.setWindowTitle(title)
        dialog.setText(text)
        dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialog.exec()


class SettingsDialog(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.ui_settings_dialog = Ui_settings_dialog()
        self.ui_settings_dialog.setupUi(self)

        self.ui_settings_dialog.lineEdit.setText(self.controller.getWorkingDir())

        self.ui_settings_dialog.btn_browse.clicked.connect(self.openDirBrowser)

        self.ui_settings_dialog.buttonBox.accepted.connect(self.setWorkingDir)

    def openDirBrowser(self):
        working_dir = QFileDialog().getExistingDirectory(self, caption="Выберите директорию")
        if working_dir:
            self.ui_settings_dialog.lineEdit.setText(working_dir)

    def setWorkingDir(self):
        if not self.controller.setWorkingDir(self.ui_settings_dialog.lineEdit.text()):
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Ошибка")
            dialog.setText("Несуществующая директория")
            dialog.setStandardButtons(QMessageBox.StandardButton.Close)
            dialog.exec()
