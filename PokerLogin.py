# Scott Smith
# Poker Log In Screen 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QLineEdit, QPushButton, QAction, QGraphicsDropShadowEffect
from PokerUI import *
from PokerAbout import *
import re
import pymysql
#import sys

class Ui_LoginWindow(QMainWindow):

        #pass database connection info 
    def __init__(self, con, connected):
        self.con = con
        self.connected = connected
        super().__init__()
        self.setStyleSheet("QMainWindow {background-image: url(images/bg.png);}")
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))


    def setupUi(self, MainWindow):                      

            #send a warning prompt: no connection 
        if not self.connected:
            self.connError()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 100, 400, 100))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        #self.label_6.setFont(font)
        #self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.setPixmap(QPixmap("images/logo.png"))

        self.verticalLayout.addWidget(self.label_6)
        #self.label_7 = QtWidgets.QLabel(self.widget)
        #self.label_7.setEnabled(True)
        #self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_7.setObjectName("label_7")

        #self.label_7.setStyleSheet("background-color: white;")

        font2 = QtGui.QFont()
        font2.setFamily("Consolas")
        font2.setPointSize(8)
        font2.setBold(True)
        #self.label_7.setFont(font2)
        #self.verticalLayout.addWidget(self.label_7)

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 200, 800, 116))
        self.widget_2.setObjectName("widget_2")

        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(50, 20, 72, 96))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("images/blue.png"))       
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(678, 20, 72, 96))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("images/blue.png"))       
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setStyleSheet("background-image: url(images/score_border.png);")


        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 200, 200))
        
        self.label_11.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.label_11.setFont(font2)

        self.label_11.setObjectName("label_11")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(600, 0, 200, 200))
        self.widget_4.setObjectName("widget_4")


        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 200, 73))
        self.label_12.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")

        self.label_12.setFont(font2)
        self.label_12.setStyleSheet("background-image: url(images/credit_border.png);")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(200, 0, 400, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)

                #list to store card labels (deck color change)
        self.cardLabels = []
        self.cardLabels.append(self.label_8)
        self.cardLabels.append(self.label_9)
        self.cardLabels.append(self.label_13)
        self.cardLabels.append(self.label_14)
        self.cardLabels.append(self.label_15)
        self.cardLabels.append(self.label_16)
        self.cardLabels.append(self.label_17)

        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(200, 250, 400, 170))
        self.widget_5.setObjectName("widget_5")

        self.widget_5.setStyleSheet("background-image: url(images/result_border.png);")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setContentsMargins(20, 10, 20, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label.setText("Username")
        self.label.setStyleSheet("background-image: url();")

        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-image: url();")
        
        self.lineEdit.setMaxLength(16)

        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_2.setText("Password")
        self.label_2.setStyleSheet("background-image: url();")

        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-image: url();")


        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setMaxLength(20)
        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton = MyPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 480, 100, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setAutoDefault(True)

        self.pushButton.clicked.connect(self.login)

        self.pushButton_4 = MyPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 480, 100, 50))
        self.pushButton_4.setObjectName("pushButton_4")        
        self.pushButton_4.clicked.connect(self.signup)
        self.pushButton_4.setAutoDefault(True)

        self.pushButton_3 = MyPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 480, 100, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setAutoDefault(True)
                 
                #                   -----------------                            QUICK PLAY LAUNCH HERE           ------------------------ 
                #use (lambda:self.openWindow()) to pass the function as parameter
                #we set username to None so we don't try to load db info when there 'is' a connection 
                
        self.pushButton_3.clicked.connect(lambda:self.openWindow(self.con, self.connected, None))

        self.pushButton_2 = MyPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 480, 100, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setAutoDefault(True)

        self.pushButton_2.clicked.connect(self.close)            
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        MainWindow.setMenuBar(self.menubar)

        self.menubar.setStyleSheet("")
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)
       
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(self.close)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.openAboutWindow)

        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())


        self.scottsLabel = QLabel(self.centralwidget)
        self.scottsLabel.setText("By Scott Smith")
        self.scottsLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scottsLabel.setStyleSheet("color:tan;")
        self.scottsLabel.setGeometry(QtCore.QRect(700, 550, 100, 50))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Poker Game Log In"))
        #self.label_6.setText(_translate("MainWindow", "Poker Game"))
        #self.label_7.setText(_translate("MainWindow", "By Scott Smith"))

                #update score list from db 
        self.highScoreList()

        self.label_12.setText(_translate("MainWindow", "\n    Credits:  "))
        #self.label.setText(_translate("MainWindow", "Username"))
        #self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Log In"))
        self.pushButton_2.setText(_translate("MainWindow", "Quit"))
        self.pushButton_3.setText(_translate("MainWindow", "Quick Play"))

        self.pushButton_4.setText(_translate("MainWindow", "Sign Up"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))        
        
        self.actionQuit.setText(_translate("MainWindow", "Quit"))    
        self.actionAbout.setText(_translate("MainWindow", "About"))
                                            
    def login(self):
                    #these aren't case sensitive, but that's the fun part. ;]
        if self.connected:
            self.username = self.lineEdit.text()
            self.password = self.lineEdit_2.text()

            with self.con:
                cur = self.con.cursor()
                    #check if credentials are correct
                query = "SELECT * FROM users WHERE username = %s AND password = %s;"
                result = cur.execute(query, (self.username, self.password))

                    #if so, 1 row will be found; grant access 
                if result > 0:
                    self.openWindow(self.con, self.connected, self.username)
                    #otherwise, user doesn't exist or wrong credentials; exit gracefully
                else:
                    self.userNotFound()
        else:
            self.connError()

    def signup(self):

        if self.connected:
            self.username = self.lineEdit.text()
            self.password = self.lineEdit_2.text()

                    #only allow alphanumeric usernames
            for i in range(len(self.username)):

                user_input = re.search('[a-zA-Z0-9]', self.username[i])
    
                    #if character is not alphanumeric show error 
                if user_input is None:
                    self.alphanumericOnly()
                    return
                    
                    #omit short log in credentials 
            if len(self.username) < 3 or len(self.password) < 3:
                self.shortCredentials()
                return

                    #'with self.con:' frees up resources and provides error handling
            with self.con:
                cur = self.con.cursor()
                    #insert username and password
                try:
                    query = "INSERT INTO users VALUES (DEFAULT, %s, %s, 'blue', 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);"
                    cur.execute(query, (self.username, self.password))

                    #confirm login created
                    self.loginValid()

                    #name already exists? flare up a messagebox
                except pymysql.err.IntegrityError:
                    self.duplicateUser()    
                
        else:
            self.connError()

                #display high score list                LETS FIX THIS TO LOAD EVERYTHING AT ONCE? is there more to load here? 
    def highScoreList(self):
         
        result = str("\n         High Scores:       \n" +
                    "    ---------------------   \n")

        if self.connected:
            with self.con:
                cur = self.con.cursor()

                    #try:
                query = "SELECT username, score FROM users WHERE user_id <> 1 ORDER BY score DESC LIMIT 9;"
                cur.execute(query)
                rs = cur.fetchall()
                for i in range(len(rs)):
                    result += "    %-16s%8s\n" % (rs[i][0], (str(rs[i][1]) + "   "))
    
        self.label_11.setText(result)

                #notify user before closing app; the closeEvent will be diff in main screen
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Poker Game',
                                        "Are you sure you want to quit?",
                                        QMessageBox.Yes | QMessageBox.No )
                #exit app
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

                #return popup information to the user depending on events         
    def shortCredentials(self):
        warning = QMessageBox.warning(self, 'Credentials too short',
                                        "Username and password must be at least 3 characters."
                                        "\nTry again.")

    def alphanumericOnly(self):
        warning = QMessageBox.warning(self, 'Unauthorized characters in Username',
                                        "Username may contain only alphanumeric characters.")

    def duplicateUser(self):
        warning = QMessageBox.warning(self, 'Duplicate Username',
                                        "Looks like that name is taken."
                                        "\nTry another.")
    def loginValid(self):
        info = QMessageBox.information(self, 'User created',
                                        "Log in to track your score and stats."
                                            "\nHave fun!")
    def userNotFound(self):
        warning = QMessageBox.warning(self, 'User not found',
                                        "Sorry, user not found.\n"
                                        "Make sure your username and password are correct.")
    def connError(self):
        warning = QMessageBox.warning(self, 'Poker Game',
                                    "Error connecting to server.\n"
                                    "Logins are not permitted at this time.\n"
                                    "Quick Play is still available.")
                             
            #open main screen here 
    def openWindow(self, con, connected, username):
        self.pokerUI = Ui_MainWindow(con, connected, username)
        self.pokerUI.setupUi(self.pokerUI)
            #hide login window
        self.hide()
            #launch main window
        self.pokerUI.show()        

    def openAboutWindow(self):
        self.aboutWin = Ui_AboutWindow()
        self.aboutWin.setupUi(self.aboutWin)
        self.aboutWin.show()


    #some shortcut keys 
    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


    #custom GUI buttons
class MyPushButton(QPushButton):

    def __init__(self, parent):
        QPushButton.__init__(self, parent)
        self.setStyleSheet('''QPushButton{background-image: url(images/pushbutton.png);
                    border-style: inset;
                    border-width: medium;
                    border-radius: 10px;
                    border-color: tan;
                    font-family: consolas;
                    font:bold;
                    font-size: 14px;} 
                    QPushButton:focus{border-color: blue;}''')


        #don't normally launch from here; testing purposes
'''        
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_LoginWindow(None, False)
    ui.setupUi(ui)
    ui.show()
    sys.exit(app.exec_())
'''    