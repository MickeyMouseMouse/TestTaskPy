from PyQt6.QtWidgets import QApplication
from Controller import Controller


if __name__ == '__main__':
    app = QApplication([])
    controller = Controller()
    app.exec()
