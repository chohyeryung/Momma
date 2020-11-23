import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from calendar import Calendar

from game_mama import Game_mama
from calendarWindow import CalendarWindow
from showDiaryWindow import ShowDiaryWindow


class Choice(QMainWindow):
    def __init__(self):
        super().__init__()
        self.choiceUI()

    def choiceUI(self):
        btnDiary=QPushButton('일기 쓰기', self)
        btnGame=QPushButton('맘마 먹자',self)
        btnShowDiary=QPushButton('일기 보기',self)

        btnDiary.move(100,100)
        btnDiary.resize(200,200)
        btnDiary.clicked.connect(self.GoDiary)

        btnGame.move(500, 100)
        btnGame.resize(200, 200)
        btnGame.clicked.connect(self.GoGame)

        btnShowDiary.move(900, 100)
        btnShowDiary.resize(200, 200)
        btnShowDiary.clicked.connect(self.ShowDiary)

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
        self.calw = CalendarWindow(self)
        self.calw.show()
        self.hide()

    def ShowDiary(self):
        self.choicesh = ShowDiaryWindow(self)
        self.choicesh.show()
        self.hide()

    def GoGame(self):
        self.gamew = Game_mama(self)
        self.gamew.show()
        self.hide()

if __name__=="__main__":
    app=QApplication(sys.argv)
    choice=Choice()
    choice.show()
    sys.exit(app.exec_())