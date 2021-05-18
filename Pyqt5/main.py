from PyQt5.QtWidgets import QApplication, QMainWindow
from pyautogui import typewrite
from time import sleep
from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.start)
        self.show()

    def start(self):
        global e2
        x = int(self.spinBox.value())

        sleep(2)
        while True:
            typewrite(self.message_entry.text())
            sleep(.600)
            typewrite("\n")

            x = x - 1

            if x == 0:
                break




if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
