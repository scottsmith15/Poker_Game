# Scott Smith Poker UI

import time
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QLabel, QComboBox, QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from Poker import *
from PokerStats import *
from PokerLogin import *
#from PokerDB import *
from PokerAbout import *

class Ui_MainWindow(QMainWindow):

            #pass database connection info and username for stats
    def __init__(self, con, connected, username):
        self.con = con
        self.connected = connected
        self.username = username
        super().__init__() 
        self.setStyleSheet("QMainWindow {background-image: url(images/bg.png);}")
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))


    def setupUi(self, MainWindow):       

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(190, 430, 420, 118))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
            #pass this window to labels to stop highlighting when not playing 
        self.label = MyLabel(self.frame, self)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        
        self.label_2 = MyLabel(self.frame, self)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        
        self.label_3 = MyLabel(self.frame, self)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = MyLabel(self.frame, self)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)


                        #test? 
        self.label_5 = MyLabel(self.frame, self)
        self.label_5.setText("") 
        self.label_5.setPixmap(QtGui.QPixmap("images/blue.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)


                    #list to traverse and swap pixmaps 
        self.listOfPlayersCards = []
        self.listOfPlayersCards.append(self.label)
        self.listOfPlayersCards.append(self.label_2)
        self.listOfPlayersCards.append(self.label_3)
        self.listOfPlayersCards.append(self.label_4)
        self.listOfPlayersCards.append(self.label_5)
        
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
        #self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_6.setPixmap(QPixmap("images/logo.png"))

        #self.label_7 = QtWidgets.QLabel(self.widget)
        #self.label_7.setEnabled(True)
        #self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_7.setObjectName("label_7")
        #self.verticalLayout.addWidget(self.label_7)

        font2 = QtGui.QFont()
        font2.setFamily("Consolas")
        font2.setPointSize(8)
        font2.setBold(True)
        #self.label_7.setFont(font2)

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 200, 800, 170))
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
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(200, 0, 400, 170))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.label_10.setStyleSheet("background-image: url(images/result_border.png);")

        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.widget_3.setObjectName("widget_3")

        self.widget_3.setStyleSheet("background-image: url(images/score_border.png);")

        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setObjectName("label_11")

        self.label_11.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.label_11.setFont(font2)

        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(600, 0, 200, 200))
        self.widget_4.setObjectName("widget_4")

        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 200, 73))
        self.label_12.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_12.setFont(font2)

        self.label_12.setStyleSheet("background-image: url(images/credit_border.png);")

        self.newHandButton = MyPushButton(self.centralwidget)
        self.newHandButton.setGeometry(QtCore.QRect(50, 340, 100, 50))
        self.newHandButton.setObjectName("newHandButton")

        self.newHandButton.clicked.connect(self.newHand)
        self.newHandButton.setAutoDefault(True)

        self.turnInHandButton = MyPushButton(self.centralwidget)
        self.turnInHandButton.setGeometry(QtCore.QRect(325, 380, 150, 50))
        self.turnInHandButton.setObjectName("turnInHandButton")

        self.turnInHandButton.clicked.connect(self.turnInHand)
        self.turnInHandButton.setAutoDefault(True)

        self.discardButton = MyPushButton(self.centralwidget)
        self.discardButton.setGeometry(QtCore.QRect(650, 340, 100, 50))
        self.discardButton.setObjectName("discardButton")

        self.discardButton.clicked.connect(self.discard)
        self.discardButton.setAutoDefault(True)

                #these allow user to use keyboard to play
        self.cardBtn1 = MyPushButton(self.centralwidget)
        self.cardBtn1.setGeometry(QtCore.QRect(201, 540, 72, 10))
        self.cardBtn1.setObjectName("cardBtn1")
        self.cardBtn1.clicked.connect(lambda:self.btnEventKeyboardPlay(0))
        self.cardBtn1.setAutoDefault(True)

        self.cardBtn2 = MyPushButton(self.centralwidget)
        self.cardBtn2.setGeometry(QtCore.QRect(283, 540, 71, 10))
        self.cardBtn2.setObjectName("cardBtn1")
        self.cardBtn2.clicked.connect(lambda:self.btnEventKeyboardPlay(1))
        self.cardBtn2.setAutoDefault(True)

        self.cardBtn3 = MyPushButton(self.centralwidget)
        self.cardBtn3.setGeometry(QtCore.QRect(364, 540, 72, 10))
        self.cardBtn3.setObjectName("cardBtn1")
        self.cardBtn3.clicked.connect(lambda:self.btnEventKeyboardPlay(2))
        self.cardBtn3.setAutoDefault(True)

        self.cardBtn4 = MyPushButton(self.centralwidget)
        self.cardBtn4.setGeometry(QtCore.QRect(446, 540, 71, 10))
        self.cardBtn4.setObjectName("cardBtn1")
        self.cardBtn4.clicked.connect(lambda:self.btnEventKeyboardPlay(3))
        self.cardBtn4.setAutoDefault(True)

        self.cardBtn5 = MyPushButton(self.centralwidget)
        self.cardBtn5.setGeometry(QtCore.QRect(527, 540, 72, 10))
        self.cardBtn5.setObjectName("cardBtn1")
        self.cardBtn5.clicked.connect(lambda:self.btnEventKeyboardPlay(4))
        self.cardBtn5.setAutoDefault(True)

        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(190, 530, 420, 40))
        self.widget_5.setObjectName("widget_5")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
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
        self.cardLabels.append(self.label)
        self.cardLabels.append(self.label_2)
        self.cardLabels.append(self.label_3)
        self.cardLabels.append(self.label_4)
        self.cardLabels.append(self.label_5)
        self.cardLabels.append(self.label_8)
        self.cardLabels.append(self.label_9)
        self.cardLabels.append(self.label_13)
        self.cardLabels.append(self.label_14)
        self.cardLabels.append(self.label_15)
        self.cardLabels.append(self.label_16)
        self.cardLabels.append(self.label_17)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        
        MainWindow.setMenuBar(self.menubar)

        self.menubar.setStyleSheet("")
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.actionBack_To_Login = QtWidgets.QAction(MainWindow)
        self.actionBack_To_Login.setObjectName("actionBack_To_Login")
        self.actionBack_To_Login.triggered.connect(self.openLoginWindow)
        
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(self.close)

        self.actionColor = QtWidgets.QAction(MainWindow)
        self.actionColor.setObjectName("actionColor")
        self.actionColor.triggered.connect(self.openCardColorWindow)     

        self.actionStats = QtWidgets.QAction(MainWindow)
        self.actionStats.setObjectName("actionStats")
        self.actionStats.triggered.connect(self.openStatsWindow)                    #FIGURE THIS OUT

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.openAboutWindow)

        self.menuFile.addAction(self.actionBack_To_Login)
        self.menuFile.addAction(self.actionQuit)
        self.menuOption.addAction(self.actionColor)
        self.menuOption.addAction(self.actionStats)
        self.menuAbout.addAction(self.actionAbout)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

            #  ------------------     these would be for the "player"; these variables show the 'state' of the game ------------------
        self.deck = Deck()
        self.hand = None
        self.cards = []
        self.limit = 0
        self.score = 0
        self.discard = False
        self.turnIn = False
            #flag for infinite loop in case both players have same cards [ace,ace,2,3,3]
        self.attempts = 0

        self.playerHandStr = ""                                    #store hand evaluation; appended with win/loss
        self.cpuHandStr = ""

        self.winner = False                                        #used to only add score when true  
        self.handsPlayed = 0                                       #used for saving and loading total hands played 
        self.handsWon = 0                                          #hands won
        self.scoreStr = str("\n    Credits: ")                       #used for showing a player's current score (db or no db) 
        self.highScoreList = str("\n         High Scores:       \n" + 
                                 "    ---------------------   \n")
        
        self.myCardColor = "blue"

            #store amount of hand rankings accumulated
        self.handRanks = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            #these correspond to db column names 
        self.rankings = ["pair", "two_pair", "three_of_a_kind", "straight", "flush", 
                        "full_house", "four_of_a_kind", "straight_flush", "royal_flush"]

        # ------------------------------------------ CPU --------------------------------------
        self.cpu_hand = None
        self.cpu_cards = []
        self.cpu_limit = 0


        self.scottsLabel = QLabel(self.centralwidget)
        self.scottsLabel.setText("By Scott Smith")
        self.scottsLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scottsLabel.setStyleSheet("color:tan;")
        self.scottsLabel.setGeometry(QtCore.QRect(700, 550, 100, 50))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            
            #start tracking time if logged in 
        if self.connected:
            self.timeOpen = time.perf_counter()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Poker Game"))
        #self.label_6.setText(_translate("MainWindow", "Poker Game"))
        #self.label_7.setText(_translate("MainWindow", "By Scott Smith"))
        self.label_10.setText(_translate("MainWindow", "Welcome to Poker Game\n"
            "Press \"New Hand\" to begin"))

            #       ----------------                    EXTRACT ALL DATA HERE                               --------------------
        self.loadPlayerStats()

        self.label_11.setText(self.highScoreList)
        self.label_12.setText(self.scoreStr + str(self.score))

        self.turnInHandButton.setText(_translate("MainWindow", "Turn in Hand"))
        self.newHandButton.setText(_translate("MainWindow", "New Hand"))
        
        self.discardButton.setText(_translate("MainWindow", "Discard"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionBack_To_Login.setText(_translate("MainWindow", "Back to Login Screen"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionColor.setText(_translate("MainWindow", "Change Deck Color"))
        self.actionStats.setText(_translate("MainWindow", "View My Statistics"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
    
        #used to block hightlighting of card labels on open
    def getHand(self):
        return self.hand

    def discard(self):
        if self.hand != None:
            if not self.turnIn:                                         #if true: you've already turned this hand in; do nothing 
                if not self.discard:
                    cardsPressed = 0
                    checkList = []
                    for i in range(len(self.listOfPlayersCards)):
                        if self.listOfPlayersCards[i].isClicked():
                            cardsPressed += 1
                            checkList.append(i)                         #make a list of card indices    
                    if cardsPressed == 0:
                        return
                    if cardsPressed <= self.limit:                      
                        if len(checkList) == 4:                         #if discarding 4, is there an ace left in the hand?
                            aceList = []                                
                            for i in range(len(self.listOfPlayersCards)):
                                if self.cards[i].getValue() == 0:       
                                    aceList.append(i)                   #gather all aces in hand 

                            for ace in aceList:                         #if an ace exists and is not being discarded, okay to discard
                                if ace not in checkList:
                                    aceList = []
                                    break
                                else:
                                    continue                            
                            if len(aceList) != 0:                       #an ace is not leftover in hand, cannot complete discard
                                self.label_10.setText("You can discard 4 cards,\nonly if you keep an Ace.")
                                self.clearHighlights()
                                return

                        self.discard = True                             #only one discard per turn    
                        for i in range(len(checkList)):
                            self.hand.discard(checkList[i])
                            self.listOfPlayersCards[checkList[i]].setPixmap(self.cards[checkList[i]].getPixmap())
                        
                        self.label_10.setText("Turn in your hand to see your score!")
                        #self.cpu_discard()

                    else:
                        self.label_10.setText("You can only discard " + str(self.limit) + " cards.\nTry again.")
                        
                    for i in range(len(checkList)):                     #clear highlighted cards
                        self.listOfPlayersCards[checkList[i]].highlightCard()
                        
                else:
                    self.label_10.setText("Only one discard per turn.\nTurn in your hand.")
                    self.clearHighlights()
        else:
            self.label_10.setText("You don't have anything to discard.\n"
                "Press \"New Hand\" to begin")


                #this could get ugly...
    def cpu_discard(self):
        return 
                #range(7, len(self.cardLabels)) is the CPU's cards
    def cpu_turnInHand(self):

        for i in range(7, len(self.cardLabels)):
            self.cardLabels[i].setPixmap(self.cpu_cards[i - 7].getPixmap())

        return self.cpu_hand.evaluateHand()

                #generate end round text display
    def isWinnerText(self):
        if self.winner:
            return "\n                 Winner!\n  Your hand:\n" + self.playerHandStr + "\n  Opponent's hand:\n" + self.cpuHandStr
        else:
            return "\n                You lose.\n  Your hand:\n" + self.playerHandStr + "\n  Opponent's hand:\n" + self.cpuHandStr

                #have to add logic to show CPU cards here; if implemented; MAKE SURE CHANGE OF DECK COLOR DOESNT OVERWRITE CPU'S CARDS!
    def turnInHand(self):
        if self.hand != None:
            if not self.turnIn:                 #if true: you've already turned this hand in; do nothing  
                self.playerHandStr = ""
                self.cpuHandStr = ""
                self.winner = False           
                self.clearHighlights()
                        #format the text results here 
                self.label_10.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
                self.playerHandStr += self.hand.evaluateHand()
                    #evaluate and show CPU's cards here 
                self.cpuHandStr += self.cpu_turnInHand()
                self.turnIn = True

                
                if self.cpu_hand.getScore() > self.hand.getScore():
                    self.label_10.setText(self.isWinnerText())
                else:
                    if self.cpu_hand.getScore() < self.hand.getScore():
                        self.winner = True
                        self.label_10.setText(self.isWinnerText())
                        self.handsWon += 1
                    else:
                        if self.cpu_hand.getScore() == self.hand.getScore(): 

                                #return for high cards
                            if self.hand.getScore() == 0:
                                    #compares both hands card by card recursively with the index (starts at 4)
                                self.compareHighCardValue(self.cpu_hand.getHighCardValue(), self.hand.getHighCardValue(), len(self.cards) - 1)
                            else:
                                    #return for straight or flush
                                if self.hand.getScore() == 4 or self.hand.getScore() == 5:
                                    self.compareHighCardValue(self.cpu_hand.getHighCardValue(), self.hand.getHighCardValue(), len(self.cards) - 1)
                                else:
                                        #return for SF or RF: go by high card then suit    
                                    if self.hand.getScore() == 8 or self.hand.getScore() == 9:
                                        self.compareHighCardValue(self.cpu_hand.getHighCardValue(), self.hand.getHighCardValue(), len(self.cards) - 1)    
                                        

                                        #return for all other hands
                                    else:
                                            #two pair and full house
                                        if self.hand.getScore() == 2 or self.hand.getScore() == 6:
                                            self.compareHighRankValue(self.cpu_hand.getHighRankValue(), self.hand.getHighRankValue(), False)

                                            # pair, TOAK, FOAK
                                        else:
                                            self.compareHighRankValue(self.cpu_hand.getHighRankValue(), self.hand.getHighRankValue(), True)
            
                    #used to track overall hand ranks 
                if self.hand.getScore() != 0:
                    self.handRanks[self.hand.getScore() - 1] += 1
                
                if self.winner:
                    self.addScore()
                else:
                    self.subScore()

                    #refresh high score list if score changed
                if not self.winner or self.hand.getScore != 0:
                    self.refreshHighScoreList()


            #used for evaluating a winner for select hands; recursive!;     all commented printouts for testing 
    def compareHighCardValue(self, cpu, player, index):

            #in the odd case of every card being the same value 
        if index == -1 or self.attempts == 4:
            #print("comparing high suit")
            self.compareHighSuit()     
            return 

        #print("cpu: " + str(cpu) + " player: " + str(player) + " -- the beginning one")

            #if aces, make dominant
        if cpu == 0:
            cpu = 13

        if player == 0:
            player = 13

        if cpu > player:
            self.label_10.setText(self.isWinnerText() + "\n     Your opponent had higher cards.  ")
        else:
            if cpu < player:
                self.winner = True
                self.label_10.setText(self.isWinnerText() + "\n         Winner by higher cards!      ")
                self.handsWon += 1 
            else:
                    #grab next high card from both hands 
                if cpu == player:

                        #if both have aces; 0 was turned into 13 above       
                    if cpu == 13:
                            #in the event of all cards matching
                        cpu = self.cpu_cards[index].getValue()
                        player = self.cards[index].getValue()
                        #print("cpu: " + str(cpu) + " player: " + str(player) + " -- the 13 one")
                        self.attempts += 1
                        self.compareHighCardValue(cpu, player, index) 
                    
                    else:

                        cpu = self.cpu_cards[index - 1].getValue()
                        player = self.cards[index - 1].getValue()

                        #print("cpu: " + str(cpu) + " player: " + str(player) + " -- the normal one")
                        self.compareHighCardValue(cpu, player, index - 1) 


    def compareHighRankValue(self, cpu, player, second):
        #print("comparing high rank ************************")

            #if aces make dominant
        if cpu == 0:
            cpu = 13
        if player == 0:
            player = 13

        if cpu > player:
            self.label_10.setText(self.isWinnerText() + "\n     Your opponent had higher ranks.  ")
        else:
            if cpu < player:
                self.winner = True
                self.label_10.setText(self.isWinnerText()+ "\n         Winner by higher ranks!      ")
                self.handsWon += 1 
            else:
                    #grab next high card from both hands 
                if cpu == player:
                        #is this the second high rank? two pair and full house ; also used for pair, TOAK, and FOAK to only look at first high rank
                    if not second:
                        cpu2 = self.findSecondHighRank(self.cpu_cards, cpu)
                        player2 = self.findSecondHighRank(self.cards, player)
                        #print("cpu: " + str(cpu2) + " player: " + str(player2))
                        self.compareHighRankValue(cpu2, player2, True)
                    else:
                        self.compareHighCardValue(self.cpu_hand.getHighCardValue(), self.hand.getHighCardValue(), len(self.cards) - 1)

    def findSecondHighRank(self, cards, value):
        for i in range(len(cards) - 1, -1, -1):
                #if ace find next highest scored rank
            if value == 13:
                if cards[i].getValue() == cards[i - 1].getValue():
                    return cards[i].getValue()
                #if anything else, find other highest rank that is not of same value
            else:
                if cards[i].getValue() != value and cards[i].getValue() == cards[i - 1].getValue():
                    return cards[i].getValue()  

    def compareHighSuit(self):
                #is the score a: high card? straight? flush? straight flush? royal flush?
        highCardScores = [0, 4, 5, 8, 9]

        if self.hand.getScore() in highCardScores:
            cpu = self.cpu_hand.getHighCardSuit()
            player = self.hand.getHighCardSuit()

            if cpu > player:
                self.label_10.setText(self.isWinnerText() + "\n    Woah!  Close one.  Loss by suit.  ")
            else:
                if cpu < player:
                    self.winner = True
                    self.label_10.setText(self.isWinnerText() + "\n    Woah!  Close one.  Win by suit!  ")
                    self.handsWon += 1 
                #is the score a pair? two pair? MAYBE NOT THESE: three of a kind? full house? four of a kind?
        else:
            cpu = self.cpu_hand.getHighRankSuit()
            player = self.hand.getHighRankSuit()

            if cpu > player:
                self.label_10.setText(self.isWinnerText() + "\n    Woah!  Close one.  Loss by suit.  ")
            else:
                if cpu < player:
                    self.winner = True
                    self.label_10.setText(self.isWinnerText() + "\n    Woah!  Close one.  Win by suit!  ")
                    self.handsWon += 1


    def newHand(self):
                                                
        if self.hand != None:                   
            if not self.turnIn:                 #new hand before turning it in? no score points        
                self.noScoreMsg()
                return 

            self.hand.discardHand()             #if already playing, discard hand
            self.cpu_hand.discardHand()

                #if out of credits, launch warning message to acquire more 
        if self.score == 0:
            self.outOfCredits()


                #reset centered text display upon drawing new hand 
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.clearHighlights()    
        self.hand = Hand(self.deck)
        self.cards = self.hand.getCards()
        self.limit = self.hand.getLimit()
        self.discard = False                    #have we discarded yet?
        self.turnIn = False                     #allow hand to be turned in again 
        self.attempts = 0
        self.handsPlayed += 1                   #is this good enough? seems to be working

        # -----------   player gets five cards first and cpu gets five cards next; this could 
        #               work like normal poker if we just draw one card at a time and loop 5 times 
        #               back and forth.. since cards are random, just keeping it simple

        self.cpu_hand = Hand(self.deck)
            #needed for discard
        self.cpu_cards = self.cpu_hand.getCards()
        self.cpu_limit = self.cpu_hand.getLimit()

        for i in range(len(self.listOfPlayersCards)):
            self.listOfPlayersCards[i].setPixmap(self.cards[i].getPixmap())

        self.label_10.setText("Select cards to discard (up to " + str(self.limit) +")\n"
            "or turn in your hand.")

        for i in range(7, len(self.cardLabels)):
            self.cardLabels[i].setPixmap(QPixmap("images/" + self.myCardColor + ".png"))
        
            #add points when you win
    def addScore(self):
        self.score += self.hand.getScore()
        self.label_12.setText(self.scoreStr + str(self.score))

            #subtract points when you lose
    def subScore(self):
        self.score -= 1
        self.label_12.setText(self.scoreStr + str(self.score))

            #keep current high score list on turn in hand (win, lose) and out of credits (+10) 
    def refreshHighScoreList(self):

        if self.connected and self.username != None:
                #refresh high score list in main app
            self.highScoreList = str("\n         High Scores:       \n" + 
                                    "    ---------------------   \n")

            with self.con:
                cur = self.con.cursor()

                self.saveScore(cur)
                self.loadHighScoreList(cur)

                #repopulate high score list with current data
            self.label_11.setText(self.highScoreList) 

            #Load all player stats
    def loadPlayerStats(self):

        if self.connected and self.username != None:
            with self.con:
                cur = self.con.cursor()

                    #try
                self.loadHighScoreList(cur)               #load high score list
                self.loadScore(cur)                       #load player score
                self.loadHandsPlayed(cur)                 #load total hands played 
                self.loadCardColor(cur)                   #load preferred card color 
                self.loadHandsWon(cur)                    #load hands won 
        
                #quick play credits assigned here 
        else:
            self.score = 10


    def loadHighScoreList(self, cur):

        query = "SELECT username, score FROM users WHERE user_id <> 1 ORDER BY score DESC LIMIT 9;"
        cur.execute(query)
        rs = cur.fetchall()
        for i in range(len(rs)):
            self.highScoreList += "    %-16s%8s\n" % (rs[i][0], (str(rs[i][1]) + "   "))


    def loadScore(self, cur):

        query = "SELECT score FROM users WHERE username = %s;" 
        cur.execute(query, (self.username))
        rs = cur.fetchone()
        self.score = rs[0]
        self.scoreStr = "    %-16s\n    Credits: " % (self.username)

    def loadHandsPlayed(self, cur):

        query = "SELECT hands_played FROM users WHERE username = %s;" 
        cur.execute(query, (self.username))
        rs = cur.fetchone()
        self.handsPlayed = rs[0]

    def loadCardColor(self, cur):

        query = "SELECT card_color FROM users WHERE username = %s;" 
        cur.execute(query, (self.username))
        rs = cur.fetchone()
        self.setCardColor(rs[0])

    def loadHandsWon(self, cur):

        query = "SELECT hands_won FROM users WHERE username = %s;"
        cur.execute(query, (self.username))
        rs = cur.fetchone()
        self.handsWon = rs[0]

            #called on application exit
    def savePlayerStats(self):
        
        if self.connected and self.username != None:    
            with self.con:
                    cur = self.con.cursor()
                    
                        #try
                    self.saveTimeElapsed(cur)               #save time played
                    self.saveScore(cur)                     #save player's score
                    self.saveHandsPlayed(cur)               #save total hands played
                    self.saveHandsWon(cur)                  #save hands won  
                    self.saveCardColor(cur)                 #save preferred card color 
                    self.saveHandRanks(cur)                 #save hand ranks (global & player)

            #called on showing player stats; needs to reset certain values so we don't double save
            #      ---- could clean these two up with a parameter passed so we only have one and an if case 
    def savePlayerStats2(self):
        
        if self.connected and self.username != None:    
            #refresh high score list in main app
            self.highScoreList = str("\n         High Scores:       \n" + 
                                    "    ---------------------   \n")
            with self.con:
                    cur = self.con.cursor()
                    
                        #try
                    self.saveTimeElapsed(cur)               #save time played
                    self.saveScore(cur)                     #save player's score
                    self.saveHandsPlayed(cur)               #save total hands played
                    self.saveHandsWon(cur)                  #save hands won  
                    self.saveCardColor(cur)                 #save preferred card color 
                    self.saveHandRanks(cur)                 #save hand ranks (global & player)
                    self.loadHighScoreList(cur)             #reload high score list in main app

                #repopulate high score list with current data
            self.label_11.setText(self.highScoreList)    

                #reset certain stats to prevent doubled saving on close 
            self.timeOpen = time.perf_counter()
            self.handRanks = [0, 0, 0, 0, 0, 0, 0, 0, 0]


    def saveScore(self, cur):
        
        query = "UPDATE users SET score = %s WHERE username = %s;" 
        cur.execute(query, (self.score, self.username))  

    def saveTimeElapsed(self, cur):

        self.timeClose = time.perf_counter()
        elapsedTime = (self.timeClose - self.timeOpen)
        seconds = round(elapsedTime)

        query = "UPDATE users SET time_played = (time_played + %s) WHERE username = %s;" 
        cur.execute(query, (seconds, self.username))  

    def saveHandsPlayed(self, cur):

        query = "UPDATE users SET hands_played = %s WHERE username = %s;" 
        cur.execute(query, (self.handsPlayed, self.username))  

    def saveHandsWon(self, cur):

        query = "UPDATE users SET hands_won = %s WHERE username = %s;"
        cur.execute(query, (self.handsWon, self.username))

    def saveCardColor(self, cur):

        query = "UPDATE users SET card_color = %s WHERE username = %s;" 
        cur.execute(query, (self.myCardColor, self.username))         

    def saveHandRanks(self, cur):
                #update global hand ranks
        for i in range(len(self.handRanks)):
            if self.handRanks[i] > 0:
                    #had to format this first before executing the query; pymysql was being difficult!!! automatically converts strings to 'string'
                    #manually in a string format, it appends as intended; hour and a half debug ;[
                query = "UPDATE users SET %s = (%s + %s) WHERE user_id = 1;" % (self.rankings[i], self.rankings[i], self.handRanks[i])
                cur.execute(query)

                    #update user hand ranks
                query = "UPDATE users SET %s = (%s + %s) WHERE username = '%s';" % (self.rankings[i], self.rankings[i], self.handRanks[i], self.username)
                cur.execute(query)

    def noScoreMsg(self):
        choice = QMessageBox.question(self, 'New Hand',
                                            "You won't get any points if you " 
                                            "draw a new hand.\nYou will still"
                                            " lose one credit.  Are you sure?",
                                            QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            self.subScore()
            self.turnIn = True
            self.refreshHighScoreList()
            self.newHand()
        else:
            return

                #notify user before closing app
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Poker Game',
                                        "Are you sure you want to quit?",
                                        QMessageBox.Yes | QMessageBox.No )
                #exit app
        if reply == QMessageBox.Yes: 
                #  ------------------------                 SAVE ALL DATA PRIOR TO CLOSE                                --------------------------
            self.savePlayerStats()
                
            event.accept()
        else:
            event.ignore()

            #allows user to select cards with tab and enter keys instead of mouse
    def btnEventKeyboardPlay(self, btnNum):
        self.listOfPlayersCards[btnNum].highlightCard()

            #clear any hanging selected cards
    def clearHighlights(self):
        for i in range(len(self.listOfPlayersCards)):                
                if self.listOfPlayersCards[i].isClicked():
                    self.listOfPlayersCards[i].highlightCard()
 
    def openCardColorWindow(self):
                
        dialog = MyDialog(self)
        dialog.setupUi(dialog)
        dialog.exec_()

    def setCardColor(self, color):
        self.myCardColor = color
        self.colorCycle(color)
        
                #to iterate through and swap deck color
    def colorCycle(self, color):

        if self.hand == None:
            for i in range(len(self.cardLabels)):
                    self.cardLabels[i].setPixmap(QtGui.QPixmap("images/" + color + ".png"))
        else:
                    #these would be CPU's cards being shown since we've turned in a hand
            if self.turnIn:
                self.label_8.setPixmap(QtGui.QPixmap("images/" + color + ".png"))
                self.label_9.setPixmap(QtGui.QPixmap("images/" + color + ".png"))
            else:
                    #only change pixmaps of cards not facing up;                INDENT IF ABOVE IS IMPLEMENTED
                for i in range(len(self.cardLabels) - 1, len(self.listOfPlayersCards) - 1, -1):
                    self.cardLabels[i].setPixmap(QtGui.QPixmap("images/" + color + ".png"))       


    def openStatsWindow(self):

        if self.connected and self.username != None:
                #save current stats to db                
            self.savePlayerStats2()
                #launch stats window
            self.statsWin = Ui_Form(self.con, self.connected, self.username)
            self.statsWin.setupUi(self.statsWin)
            self.statsWin.show()

        else:
            self.quickPlayStatError()

    def connError(self):
        warning = QMessageBox.warning(self, 'Poker Game',
                                    "Error connecting to server.\n"
                                    "Stats are not viewable at this time.")
    
        #credit system
    def outOfCredits(self):
        info = QMessageBox.information(self, 'Out of Credits',
                                        "Looks like you've ran out of credits.\n"
                                        "No worries, enjoy some more on us!\n"
                                        "Have fun playing!")

        self.score = 10
        self.label_12.setText(self.scoreStr + str(self.score))
        self.refreshHighScoreList()

    def quickPlayStatError(self):
        warning = QMessageBox.warning(self, 'Poker Game',
                                    "Stats are not viewable in Quick Play.")

    def openLoginWindow(self):

        if self.connected and self.username != None:
            reply = QMessageBox.question(self, 'Poker Game',
                                            "Are you sure you want to go back to the login screen?\n"
                                            "Your stats will be saved upon exiting.",
                                            QMessageBox.Yes | QMessageBox.No )
                #back to login for quickplay 
        else:
            reply = QMessageBox.question(self, 'Poker Game',
                                            "Are you sure you want to go back to the login screen?",
                                            QMessageBox.Yes | QMessageBox.No )

        if reply == QMessageBox.Yes: 
                #  ------------------------                 SAVE ALL DATA PRIOR TO LOGIN SCREEN                          --------------------------

            self.savePlayerStats()
            self.hide()
                #launches main app without cmd console popping up ;]
            subprocess.Popen("PokerMain.py", shell=True)
        else:
            return


    def openAboutWindow(self):
        self.aboutWin = Ui_AboutWindow()
        self.aboutWin.setupUi(self.aboutWin)
        self.aboutWin.show()

            #some shortcut keys 
    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

            #for selecting deck color 
class MyDialog(QDialog):
            #parent window is for passing back the color choice 
    def __init__(self, parentWindow):
        super().__init__()
        self.parentWindow = parentWindow
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))
        self.setStyleSheet("QDialog {background-image: url(images/deckcolor.png);}")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
            #gets rid of '?'
        Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)


        '''
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(75, 150, 150, 30))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        '''

        self.okButton = MyPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(50, 150, 75, 50))
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(self.accept)
        self.okButton.setAutoDefault(True)
        self.okButton.setText("OK")

        self.cancelButton = MyPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(175, 150, 75, 50))
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.clicked.connect(self.reject)
        self.cancelButton.setAutoDefault(True)
        self.cancelButton.setText("Cancel")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(50, 20, 200, 100))
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("background-image: url(images/pushbutton.png);")

        self.comboBox.setIconSize(QSize(72, 96))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)

        self.comboBox.addItem(QIcon("images/blue.png"), "Blue")
        self.comboBox.addItem(QIcon("images/red.png"), "Red")
        self.comboBox.addItem(QIcon("images/yellow.png"), "Yellow")
        self.comboBox.addItem(QIcon("images/green.png"), "Green")
        self.comboBox.addItem(QIcon("images/purple.png"), "Purple")

        self.retranslateUi(Dialog)

                #overridden below 
        #self.buttonBox.accepted.connect(Dialog.accept)
        #self.buttonBox.rejected.connect(Dialog.reject)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Choose Deck Color"))

    def accept(self):
        if self.comboBox.currentIndex() == 0:
            self.parentWindow.setCardColor("blue")
        else:
            if self.comboBox.currentIndex() == 1:
                self.parentWindow.setCardColor("red")
            else:
                if self.comboBox.currentIndex() == 2:
                    self.parentWindow.setCardColor("yellow")
                else:
                    if self.comboBox.currentIndex() == 3:
                        self.parentWindow.setCardColor("green")
                    else:
                        if self.comboBox.currentIndex() == 4:
                            self.parentWindow.setCardColor("purple") 
        self.close()

    def reject(self):
        self.close() 
    
    def closeEvent(self, event):
        event.accept()

            #custom labels for selecting cards
                                #Make it so the actual cards must be showing to be clicked, no card backs! to keep it clean :]
                                #also, if user has red cards, highlight blue instead! could be cool ::not needed really...
class MyLabel(QLabel):
            #slightly different constructor to inherit from parent
    def __init__(self, parent, parentWindow):
        QLabel.__init__(self, parent)
        self.parentWindow = parentWindow
        self.clicked = False

            #highlight a card for discard ;         COULD MAKE THIS SELECT THE CORRESPONDING PUSHBUTTON **********************
    def mousePressEvent(self, event):
        self.highlightCard()

    def highlightCard(self):
        if self.parentWindow.getHand() != None:
            if not self.clicked:
                self.setStyleSheet('''QLabel {border-style: inset;
                    border-width: medium;
                    border-radius: 20px;
                    border-color: red;
                    }''')
                self.clicked = True
            else: 
                self.setStyleSheet('')
                self.clicked = False

            #for traversing the list of cards that are selected 
    def isClicked(self):
        return self.clicked


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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    connection = DB_Connect()
    con = connection.getCon()
    connected = connection.isConnected()

    ui = Ui_MainWindow(con, connected, "scott")
    ui.setupUi(ui)
    ui.show()
    sys.exit(app.exec_())
'''    
    #test for card color dialog window
'''
import sys
app = QtWidgets.QApplication(sys.argv)
demo = MyDialog()
demo.setupUi(demo)
demo.show()
sys.exit(app.exec_())
'''