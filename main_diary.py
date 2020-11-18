from PyQt5.QtGui import QIcon

from calenderWindow import Calender
from choice import Choice
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Main_Diary(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Momma')
        self.setWindowIcon(QIcon('baby.png'))
        self.setGeometry(300, 100, 1200, 800)


if __name__=="__main__":
    app=QApplication(sys.argv)
    main=Main_Diary()
    main.show()
    sys.exit(app.exec_())