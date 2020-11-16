import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from calender import Calender

class Choice(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnDiary=QPushButton('일기 쓰기', self)
        btnGame=QPushButton('맘마 먹자',self)
        btnShowDiary=QPushButton('일기 보기',self)

        btnDiary.move(100,100)
        btnDiary.resize(200,200)
        btnDiary.clicked.connect(self.GoDiary)

        btnGame.move(500, 100)
        btnGame.resize(200, 200)
        # btnGame.clicked.connect(self.GoGame)

        btnShowDiary.move(900, 100)
        btnShowDiary.resize(200, 200)
        #btnShowDiary.clicked.connect(self.ShowDiary)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(btnDiary)
        vbox.addWidget(btnGame)
        vbox.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self.setLayout(hbox)
        self.setWindowTitle('Momma')
        self.setWindowIcon(QIcon('baby.png'))
        self.setGeometry(300,100,1200,800)
        self.show()

    def GoDiary(self):
        print('눌렀따')
        self.hide()
        self.ex=Calender()
        self.ex.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    main=Choice()
    main.show()
    sys.exit(app.exec_())