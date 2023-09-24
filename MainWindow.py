from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QPointF, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QColor


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(400, 460)
        font = QtGui.QFont()
        font.setPointSize(16)
        main_window.setFont(font)
        main_window.setStyleSheet("QMainWindow {\n"
                                  "    background-color: white;\n"
                                  "}")
        self.centralwidget = QtWidgets.QWidget(parent=main_window)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_logo.setStyleSheet("margin: 3em 0em 2.2em 1.5em;")
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_logo.setObjectName("label_logo")
        self.verticalLayout.addWidget(self.label_logo)
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.comboBox.setStyleSheet("QComboBox {\n"
                                    "    border: 2px solid black;\n"
                                    "    padding: 0.7em 1em;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "  color: black;    \n"
                                    "  background-color: white;\n"
                                    "  selection-background-color: blue;\n"
                                    "}")
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_status = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_status.setFont(font)
        self.label_status.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_status.setStyleSheet("margin-top: 1.2em;\n"
                                        "margin-bottom: 0.4em;\n"
                                        "color: #6c6c6c;")
        self.label_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.verticalLayout.addWidget(self.label_status)
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    border: 2px solid black;\n"
                                       "    padding: 0.5em 1em;\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "    background-color: #48ce57;\n"
                                       "}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_start = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("QPushButton {\n"
                                     "    font-weight: bold;\n"
                                     "    color: black;\n"
                                     "    background-color: white;\n"
                                     "    border: 2px solid black;\n"
                                     "    border-radius: 5px;\n"
                                     "    padding: 0.7em 4.5em;\n"
                                     "    margin-top: 2em;\n"
                                     "    margin-bottom: 1.5em;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: #a0a0a0;\n"
                                     "}")

        shadow_effect = QtWidgets.QGraphicsDropShadowEffect()
        shadow_effect.setColor(QColor("grey"))
        shadow_effect.setOffset(QPointF(3, 3))
        shadow_effect.setBlurRadius(5)
        self.btn_start.setGraphicsEffect(shadow_effect)

        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        main_window.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")

        self.menu = CustomMenu(parent=self.menubar)

        self.menu.setObjectName("menu")
        main_window.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(main_window)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Геопортал"))
        self.comboBox.setItemText(0, _translate("main_window", "v1"))
        self.comboBox.setItemText(1, _translate("main_window", "v2"))
        self.label_status.setText(_translate("main_window", "Выберите тип и нажмите Запуск"))
        self.btn_start.setText(_translate("main_window", "Запуск"))
        self.menu.setTitle(_translate("main_window", "Настройки"))


class CustomMenu(QtWidgets.QMenu):
    signal_click = pyqtSignal(str)

    def __init__(self, parent = None):
        super(CustomMenu, self).__init__(parent)

    @pyqtSlot()
    def mouseReleaseEvent(self, event):
        self.signal_click.emit("clicked")
