


from PyQt5 import QtCore, QtGui, QtWidgets
import serial


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
#       self.ser = serial.Serial('/dev/ttyACM0', 9600)

        try:
            # Initialize the Serial connection to the Arduino
            self.serial_connection = serial.Serial('COM5', 9600, timeout=1)  # Adjust the COM port as needed
        except serial.SerialException as e:
            print(f"Error: {e}")
            # Handle the exception, e.g., by displaying an error message to the user
        # ... (rest of your class methods)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 90, 71, 16))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.rotationspeedSlider = QtWidgets.QSlider(self.centralwidget)
        self.rotationspeedSlider.setGeometry(QtCore.QRect(20, 200, 131, 22))
        self.rotationspeedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rotationspeedSlider.setObjectName("rotationspeedSlider")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(210, 50, 71, 31))
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 200, 21, 16))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 50, 141, 31))
        self.label_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 10, 361, 31))
        self.label_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 170, 91, 31))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 160, 91, 31))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 200, 31, 16))
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.forwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.forwardButton.setGeometry(QtCore.QRect(100, 100, 61, 51))
        self.forwardButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-image: url(:/images/images.png);")
        self.forwardButton.setText("")
        self.forwardButton.setObjectName("forwardButton")
        self.forwardButton.clicked.connect(self.moveForward)

        
        self.backwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.backwardButton.setGeometry(QtCore.QRect(10, 100, 71, 51))
        self.backwardButton.setStyleSheet("border-image: url(:/images/Previous-Button-PNG-Images.png);")
        self.backwardButton.setText("")
        self.backwardButton.setObjectName("backwardButton")
        self.backwardButton.clicked.connect(self.moveBackward)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(190, 120, 121, 31))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textPosition")
        self.textProgress = QtWidgets.QTextBrowser(self.centralwidget)
        self.textProgress.setGeometry(QtCore.QRect(190, 190, 121, 31))
        self.textProgress.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textProgress.setObjectName("textBrowser_2")
        self.position = 1  # Initial position

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Position"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "N DIVISIONS"))
        self.label_7.setText(_translate("MainWindow", "Hybride Dividing Head Shield \"LG18\""))
        self.label.setText(_translate("MainWindow", "N[1/min]"))
        self.label_2.setText(_translate("MainWindow", "Progress"))
        self.label_4.setText(_translate("MainWindow", "480"))
    def moveForward(self):
        if self.serial_connection and self.serial_connection.is_open:

            if self.position < self.spinBox.value():
                self.position += 1
                self.updatePosition()
                self.serial_connection.write(b'F')  # Send 'F' to Arduino


    def moveBackward(self):
        # Function to move backward

        if self.serial_connection and self.serial_connection.is_open:
            if self.position > 1 and self.position <= self.spinBox.value():
                self.position -= 1
                self.updatePosition()
                self.serial_connection.write(b'B')  # Send 'B' to Arduino

    def sliderValueChanged(self, value):
        # Function to handle slider value change
        n_divisions = self.spinBox.value()
        progress = (self.position * 100) / n_divisions
        self.textProgress.setText(f"{progress:.2f}%")

        # Calculate the speed based on the slider value (adjust the range as needed)
        min_speed = 1  # Minimum speed
        max_speed = 480  # Maximum speed
        speed = min_speed + (max_speed - min_speed) * value / 100

        # Send the speed to the Arduino (you may need to format it as needed for your Arduino code)
        speed_str = f"S{int(speed)}"  # Assuming your Arduino expects a command like "Sxxx" for speed
        self.serial_connection.write(speed_str.encode())
    def updatePosition(self):
        # Update the position QLineEdit
        self.textBrowser.setText(str(self.position))
    
    # Calculate and update the progress as a percentage
        current_value_spinbox = self.spinBox.value()
        if current_value_spinbox > 0:
            progress_percentage = (self.position * 100) / current_value_spinbox
            self.textProgress.setText(f"{progress_percentage:.2f}%")
        else:
            self.textProgress.setText("0.00%")
        
    
    
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.rotationspeedSlider.valueChanged.connect(ui.sliderValueChanged)

    ui.position = ui.spinBox.value()
    MainWindow.show()
    sys.exit(app.exec_())
