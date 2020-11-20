import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ShowDiaryWindow(QMainWindow):
    def __init__(self,choice_window):
        super().__init__()
        self.choice_window=choice_window

        # 윈도우 설정
        self.setGeometry(300, 100, 1200, 800)  # x, y, w, h
        self.setWindowTitle('일기 보기')

        self.setupUI()

    def setupUI(self):
        goHome = QPushButton("홈으로", self)
        goHome.setGeometry(650, 650, 80, 30)
        goHome.clicked.connect(self.exist)

        btnShow=QPushButton("일기 보기", self)
        btnShow.setGeometry(450, 650, 80, 30)
        btnShow.clicked.connect(self.showDiary)

    def showDiary(self):
        file=open('diary.txt', 'r', encoding='utf-8')
        for f in range(file.__sizeof__()):
            line=f.readline()
            print(line)

    def exist(self):
        self.hide()
        ch = self.choice_window
        ch.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showWindow = ShowDiaryWindow()
    showWindow.show()
    sys.exit(app.exec_())