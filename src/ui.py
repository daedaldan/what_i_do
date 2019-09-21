from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from src.gsheet_io import GSheetIO
from datetime import datetime


class Window(QWidget):
    """UI for the app"""
    def __init__(self, sheetName):
        QWidget.__init__(self)
        # setting layout and widgets
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.startBtn = self.createSetStart()
        self.timerDisplay = self.createTimerDisplay()
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerTick)
        # setting values to control button and timer
        self.min = 0;
        self.sec = 0;
        self.start = True
        # setting values for writing task info to GSheet
        self.taskName = "undefined"
        self.taskStart = datetime(1, 2, 3, 4, 5, 6)
        self.taskEnd = datetime(1, 2, 3, 4, 5, 6)
        # initializing GSheetIO
        self.sheetIO = GSheetIO(sheetName)

    def createSetStart(self):
        """initialize the textbox and start task button"""
        setStart = QHBoxLayout()
        taskNameField = QLineEdit()
        startBtn = QPushButton("Start")
        startBtn.clicked.connect(self.startClick)
        setStart.addWidget(taskNameField)
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
            # setting button info
            self.start = False
            self.startBtn.setText("Stop")
            self.timer.start(1000)
            # setting IO info
            self.taskName = self.layout.itemAt(0).itemAt(0).widget().text()
            self.taskStart = datetime.today()
        else:
            # setting button info
            self.start = True
            self.startBtn.setText("Start")
            # setting timer info
            self.timer.stop()
            self.min = 0
            self.sec = 0
            # writing to GSheet
            self.taskEnd = datetime.today()
            self.sheetIO.writeTask(self.taskName, self.taskStart, self.taskEnd, self.taskEnd-self.taskStart)

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
