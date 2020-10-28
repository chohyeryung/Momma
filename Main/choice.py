import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.uic.properties import QtWidgets

from Diary.diary import Diary


class Choice(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnDiary=QPushButton('일기 쓰기', self)
        btnGame=QPushButton('맘마 먹자',self)

        btnDiary.move(100,100)
        btnDiary.resize(300,300)
        btnDiary.clicked.connect(self.GoDiary)

        btnGame.move(500, 100)
        btnGame.resize(300, 300)
        # btnGame.clicked.connect(self.GoGame)

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
        self.hide()
        self.ex=Diary()
        self.ex.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    main=Choice()
    main.show()
    sys.exit(app.exec_())