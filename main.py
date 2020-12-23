# Top Learner 
# Dice Rolling Simulator
import sys
import random
from PyQt5 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Rolling...')
        self.resize(300, 200)
        self.move(400,300)
        self.diceNumber = 0
        self.layout = QtWidgets.QGridLayout()

        self.label_1 = QtWidgets.QLabel("Click to Roll Button")
        self.label_ = QtWidgets.QLabel("")

        self.label_.setStyleSheet("background-color: yellow;border: 1px solid black;")
        self.label_.setFont(QtGui.QFont(
            'Arial',
            10,
            weight=QtGui.QFont.Bold,
        ))

        self.buttonRoll = QtWidgets.QPushButton('Roll')
        self.buttonRoll.clicked.connect(self.roll)

        self.buttonClose = QtWidgets.QPushButton('Close')
        self.buttonClose.clicked.connect(self.close)

        self.layout.addWidget(self.buttonRoll)
        self.layout.addWidget(self.buttonClose)

        self.layout.addWidget(self.label_1)
        self.layout.addWidget(self.label_)
        self.setLayout(self.layout)

    def getInteger(self):
        i, okPressed = QtWidgets.QInputDialog.getInt(self, "Get Dices","Number of Dices:", 1, 1, 3, 1)
        if okPressed:
            self.diceNumber = i
            self.show()

    def roll(self):
        min = 0
        max = 6
        rantDice = []
        for _ in range(int(self.diceNumber)):
            temp = random.randint(min, max)
            rantDice.append(temp)

        self.label_1.setText("Rolling the dices...")

        if len(rantDice) == 1:
            text = f"The value are.... {rantDice[0]}"
            self.label_.setText(text)

        if len(rantDice) == 2:
            text = f"The values are....{rantDice[0]} - {rantDice[1]}"
            self.label_.setText(text)

        if len(rantDice) == 3:
            text = f"The values are....{rantDice[0]} - {rantDice[1]} - {rantDice[2]}"
            self.label_.setText(text)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.getInteger()
    sys.exit(app.exec_())