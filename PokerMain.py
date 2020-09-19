# Scott Smith
# Poker Main

from PyQt5 import QtWidgets
#from PokerAbout import *
#from PokerStats import *
from PokerDB import *
from PokerLogin import *
#from PokerUI import *
#from Poker import * 
import sys

	
		#if __name__ == "__main__" means we're launching from here
		#			----------------										LAUNCH APP                                            -----------------
if __name__ == "__main__":

		#establish DB connection 
	connection = DB_Connect()
	con = connection.getCon()
	connected = connection.isConnected()

		#launch application :]
	app = QtWidgets.QApplication(sys.argv)
	ui = Ui_LoginWindow(con, connected)
	ui.setupUi(ui)
	ui.show()
	sys.exit(app.exec_())