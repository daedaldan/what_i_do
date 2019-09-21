from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from src.gsheet_io import GSheetIO

class Window(QWidget):
    """UI for the app"""
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.startBtn = self.createSetStart()
        self.timerDisplay = self.createTimerDisplay()
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerTick)
        self.min = 0;
        self.sec = 0;
        self.start = True

    def createSetStart(self):
        """initialize the textbox and start task button"""
        setStart = QHBoxLayout()
        taskName = QLineEdit()
        startBtn = QPushButton("Start")
        startBtn.clicked.connect(self.startClick)
        setStart.addWidget(taskName)
        setStart.addWidget(startBtn)
        self.layout.addLayout(setStart)
        return startBtn

    def createTimerDisplay(self):
        """initialize the timer display"""
        timerDisplay = QLabel("00:00")
        self.layout.addWidget(timerDisplay)
        return timerDisplay

    def startClick(self):
        if self.start:
            self.start = False
            self.startBtn.setText("Stop")
            self.timer.start(1000)
        else:
            self.start = True
            self.startBtn.setText("Start")
            self.timer.stop()
            self.min = 0
            self.sec = 0

    def timerTick(self):
        if self.sec < 10 and self.min < 10:
            self.timerDisplay.setText("0" + str(self.min) + ":" + "0" + str(self.sec))
        elif self.sec < 10:
            self.timerDisplay.setText(str(self.min) + ":" + "0" + str(self.sec))
        elif self.min < 10:
            self.timerDisplay.setText("0" + str(self.min) + ":" + str(self.sec))
        else:
            self.timerDisplay.setText(str(self.min) + ":" + str(self.sec))

        self.sec += 1
        if self.sec == 60:
            self.min += 1
            self.sec = 0
