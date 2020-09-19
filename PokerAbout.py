#Scott Smith
#Poker About Page


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
import time

class Ui_AboutWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("QMainWindow {background-image: url(images/about.png);}")
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 20, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        #self.label_6.setFont(font)
        #self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.setPixmap(QtGui.QPixmap("images/logoblue.png"))

        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(0, 130, 400, 170))
        self.widget_5.setObjectName("widget_5")


                #--------------------------HOW COME THESE I NEED URL(); AND NOT IN POKERUI LABEL 11 & 12 ----------------------------------------
        self.widget_5.setStyleSheet("background-image: url(images/result_border.png);")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setContentsMargins(20, 10, 20, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        font.setBold(True)
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 380, 30))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_7.setStyleSheet("background-image: url();")
        self.label_7.setFont(font)

        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 380, 60))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_8.setStyleSheet("background-image: url();")
        self.label_8.setFont(font)

        self.label_9 = QtWidgets.QLabel(self.widget_5)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 380, 60))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_9.setStyleSheet("background-image: url();")
        self.label_9.setFont(font)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(56, 302, 72, 96))
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(128, 302, 72, 96))
        self.label_2.setObjectName("label_2")
        self.label_2.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 302, 72, 96))
        self.label_3.setObjectName("label_3")
        self.label_3.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(272, 302, 72, 96))
        self.label_4.setObjectName("label_4")
        self.label_4.setPixmap(QtGui.QPixmap("images/blue.png"))
        
        self.images = []
        self.images.append(self.label)
        self.images.append(self.label_2)
        self.images.append(self.label_3)
        self.images.append(self.label_4)
        self.colors = ["blue", "red", "yellow", "green", "purple"]

        MainWindow.setCentralWidget(self.centralwidget)
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

            #animate about screen
        self.animate()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "About"))
        #self.label_6.setText(_translate("MainWindow", "Poker Game"))
        self.label_7.setText(_translate("MainWindow", "By Scott Smith"))
        self.label_8.setText(_translate("MainWindow", "A Brookdale Community College \n"
            "Computer Science Project \n2020"))
        self.label_9.setText(_translate("MainWindow", "Thank you to all my professors and fellow students!\n"
            "I have learned so much from all of you."))
           

    def animate(self):
            #timer for changing images
        self.timer = QTimer()
            #iterators 
        self.i = 0
        self.j = 1
            #total count if a user leaves about window open
        self.counter = 0 
            #interval and connection (which function to run at interval)
        self.timer.setInterval(500)
        self.timer.timeout.connect(lambda:self.swapImages())
            #start animation
        self.timer.start()

    def swapImages(self):
        self.images[self.i].setPixmap(QtGui.QPixmap("images/" + self.colors[self.j] + ".png"))   
        self.i += 1
        self.j += 1
        if self.i == len(self.images):
            self.i = 0
        if self.j == len(self.colors):
            self.j = 0
        self.counter += 1
            #stop animation after a set amount of time
        if self.counter == 20:
            self.timer.stop()
                #show some jokers as an easter egg
            for j in range(len(self.images)):
                self.images[j].setPixmap(QtGui.QPixmap("images/joker_black.png"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_AboutWindow()
    ui.setupUi(ui)
    ui.show()          
    sys.exit(app.exec_())
'''