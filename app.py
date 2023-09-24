from Model import Model
from Controller import Controller
from PyQt6.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication([])
    model = Model()
    controller = Controller(model)
    app.exec()
