#Scott Smith
#Poker DB 

import pymysql


class DB_Connect():
	def __init__(self): 
				#database connection variable
		self.con = None
		        #do not allow database functionality if connection error
		self.connected = True

				#establish connection
		try:
		    self.con = pymysql.connect('127.0.0.1', 'root', '', 'poker')

		        #if connection error, do not allow db functionality; QP is still available for play 
		except (ConnectionRefusedError, pymysql.err.OperationalError):
			self.con = None
			self.connected = False

	def isConnected(self):
		return self.connected

	def getCon(self):
		return self.con