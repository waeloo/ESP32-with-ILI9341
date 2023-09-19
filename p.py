import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Add a QLineEdit for position
        self.positionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.positionLineEdit.setGeometry(QtCore.QRect(50, 100, 120, 30))
        self.positionLineEdit.setObjectName("positionLineEdit")
        self.positionLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.positionLineEdit.setReadOnly(True)
        self.position = 1  # Initial position

        # Add Forward and Backward buttons
        self.forwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.forwardButton.setGeometry(QtCore.QRect(50, 140, 80, 30))
        self.forwardButton.setObjectName("forwardButton")
        self.forwardButton.setText("Forward")
        self.forwardButton.clicked.connect(self.moveForward)

        self.backwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.backwardButton.setGeometry(QtCore.QRect(160, 140, 80, 30))
        self.backwardButton.setObjectName("backwardButton")
        self.backwardButton.setText("Backward")
        self.backwardButton.clicked.connect(self.moveBackward)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dividing Head Control"))

    def moveForward(self):
        # Function to move forward
        self.position += 1
        self.updatePosition()

    def moveBackward(self):
        # Function to move backward
        if self.position > 1:
            self.position -= 1
            self.updatePosition()

    def updatePosition(self):
        # Update the position QLineEdit
        self.positionLineEdit.setText(str(self.position))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())