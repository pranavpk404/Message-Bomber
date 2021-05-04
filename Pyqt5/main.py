from PyQt5.QtCore import QCoreApplication, QMetaObject
from PyQt5.QtGui import  QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QApplication, QMainWindow, QLabel, QTabWidget,QSpinBox

import pyautogui
from time import sleep


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        def brain():
            global e2
            x = int(self.spinBox.value())

            sleep(2)
            while True:
                pyautogui.typewrite(self.message_entry.text())
                sleep(.600)
                pyautogui.typewrite("\n")

                x = x - 1

                if x == 0:
                    break

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 113)
        icon = QIcon()
        icon.addPixmap(QPixmap("icon.ico"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.message_label = QLabel(self.centralwidget)
        self.message_label.setObjectName("message_label")

        self.gridLayout.addWidget(self.message_label, 0, 0, 1, 1)

        self.message_entry = QLineEdit(self.centralwidget)
        self.message_entry.setObjectName("message_entry")

        self.gridLayout.addWidget(self.message_entry, 0, 1, 1, 2)

        self.repeat_label = QLabel(self.centralwidget)
        self.repeat_label.setObjectName("repeat_label")

        self.gridLayout.addWidget(self.repeat_label, 1, 0, 1, 2)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")

        self.gridLayout.addWidget(self.spinBox, 1, 2, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(brain)
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message Bomber"))
        self.message_label.setText(_translate("MainWindow", "Message"))
        self.repeat_label.setText(_translate("MainWindow", "Times to repeat the message"))
        self.pushButton.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
