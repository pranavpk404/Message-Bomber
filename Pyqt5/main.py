
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        def brain():
            global e2
            x = int(self.spinBox.value())
            import pyautogui
            from time import sleep
            sleep(2)
            while True:      
                pyautogui.typewrite( self.message_entry.text() )  
                sleep(.600)                     
                pyautogui.typewrite("\n")          

                x = x - 1        

                if x == 0:       
                    break 

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 113)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.message_label = QtWidgets.QLabel(self.centralwidget)
        self.message_label.setObjectName("message_label")

        self.gridLayout.addWidget(self.message_label, 0, 0, 1, 1)

        self.message_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.message_entry.setObjectName("message_entry")

        self.gridLayout.addWidget(self.message_entry, 0, 1, 1, 2)

        self.repeat_label = QtWidgets.QLabel(self.centralwidget)
        self.repeat_label.setObjectName("repeat_label")

        self.gridLayout.addWidget(self.repeat_label, 1, 0, 1, 2)

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")

        self.gridLayout.addWidget(self.spinBox, 1, 2, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(brain)
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message Bomber"))
        self.message_label.setText(_translate("MainWindow", "Message"))
        self.repeat_label.setText(_translate("MainWindow", "Times to repeat the message"))
        self.pushButton.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


