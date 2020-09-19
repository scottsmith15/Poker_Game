#Scott Smith --- Poker Game 

import sys
import random
from random import shuffle
from PyQt5 import QtCore, QtGui, QtWidgets

			#five card poker
HANDSIZE = 5
RANKS = {"Ace": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "Jack": 10, "Queen": 11, "King": 12}
SUITS = ["Clubs", "Spades", "Hearts", "Diamonds"]
SCORES = {1: "Pair", 2: "Two Pair", 3: "Three of a Kind", 4: "Straight", 5: "Flush", 
			6: "Full House", 7: "Four of a Kind", 8: "Straight Flush", 9: "Royal Flush"}

pixNum = 1					#used for automating pixmap assignment 

class Card:

	def __init__(self, rank, suit):
		
		global pixNum 

		self.rank = rank
		self.suit = suit
		self.value = int(RANKS[self.rank])
		self.pixmap = QtGui.QPixmap('images/' + str(pixNum) + '.png')
		pixNum += 1

	def getRank(self):
		return self.rank

	def getSuit(self):
		return self.suit

	def getValue(self):
		return self.value

	def getPixmap(self):							 					
		return self.pixmap

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:

	def __init__(self):

					#temporary royal flush set up; disregard images in game: correspond to numbers in /images directory so will be off
		#self.contents = [Card("Ace","Spades"), Card("10","Spades"), Card("Jack","Spades"), Card("Queen","Spades"), Card("King","Spades"), Card("Ace","Clubs"), Card("10","Clubs"), Card("Jack","Clubs"), Card("Queen","Clubs"), Card("King","Clubs")]

					#temporary straight flush set up
		#self.contents = [Card("2","Spades"), Card("3","Spades"), Card("4","Spades"), Card("5","Spades"), Card("6","Spades"), Card("2","Clubs"), Card("3","Clubs"), Card("4","Clubs"), Card("5","Clubs"), Card("6","Clubs")]

		self.contents = [Card(rank, suit) for rank in RANKS for suit in SUITS]		
		self.discardPile = []
		self.shuffle()				#temporarily comment (major debug)

	def shuffle(self):
		random.shuffle(self.contents)	#temporarily comment 
		return 

	def drawCard(self):
		if len(self.contents) > 0:
			return self.contents.pop(0)
		else:
			self.contents = self.discardPile
			self.discardPile = []
			self.shuffle()
			return self.contents.pop(0)	

			#analysis method
	def displayDeck(self):
		for i in range(len(self.contents)):
			print(self.contents[i])

			#analysis method
	def displayDiscardPile(self):
		for i in range(len(self.discardPile)):
			print(self.discardPile[i])

class Hand:

	def __init__(self, deck):
		
		self.deck = deck
		self.cards = []
		self.values = []
		self.highCard = ""
		self.highRank = ""			#used for distinguishing two similar scores: pair vs pair
		self.highCardValue = 0		#distinguishing high cards (not always the high rank value)
		self.highRankValue = 0		#distinguishing pairs 
		self.highCardSuit = ""		#distinguishing by suits if all cards equal
		self.highRankSuit = ""		#"    "    "    "    "    "
		self.score = 0
		self.straight = False    	
		self.flush = False
		#self.finalResult = ""		#don't think i'm using this 
		self.limit = 3				#total number of cards allowed to turn in each hand 
		self.evaluated = False 		#have we checked this hand already? do not evaluate again


		for i in range(HANDSIZE):
			self.cards.append(self.deck.drawCard())

			#set a discard limit at beginning of hand; if any card is an ace, can draw up to 4 new cards
		if any(card for card in self.cards if card.getValue() == 0):
			self.limit += 1

	def getCards(self):
		return self.cards

	def getLimit(self):
		return self.limit

	def getHighRank(self):
		return self.highRank

	def getHighRankValue(self):
		return self.highRankValue

	def getHighRankSuit(self):
		return self.highRankSuit

	def getHighCardValue(self):
		return self.highCardValue

	def getHighCardSuit(self):
		return self.highCardSuit

	def getScore(self):
		return self.score

			#analysis method
	def showHand(self):
		for i in range(HANDSIZE):
			print(self.cards[i])

			#sort hand and create list of values for evaluation
	def sortHand(self):
		self.cards.sort(key=lambda card: card.getValue())
		for i in range(HANDSIZE):
			self.values.append(self.cards[i].getValue())

	def discard(self, index):
		self.deck.discardPile.insert(0, self.cards.pop(index))
			#to keep integrity of the list, add new card to same location 
		self.cards.insert(index, self.deck.drawCard())	
		
	def discardHand(self):		
			#after hand has been evaluated; end of turn
		for i in range(HANDSIZE):
			self.deck.discardPile.insert(0, self.cards.pop())			#create a new Hand(); keep same deck; done in UI module


	def isStraight(self): 
				#sort hand and create a list of values
		self.sortHand()
				#check if ace high
		if self.values[0] == 0 and self.values[-1] == 12:
			for i in range(HANDSIZE - 1, 1, -1):
				if (self.values[i] - self.values[i - 1] == 1):
					continue
				else:
					return 

				#otherwise check for normal straight 
		else:
			for i in range(HANDSIZE - 1):
				if (self.values[i] + 1 == self.values[i + 1]):
					continue
				else:
					return 

				#return score of straight and set straight to true 
		self.straight = True
		self.score = 4
		return 

	def isFlush(self):
				#all cards in hand one suit?
		firstSuit = self.cards[0].getSuit()

		for i in range(1, HANDSIZE):
			if self.cards[i].getSuit() == firstSuit:
				continue
			else:
				return 
		self.flush = True
		self.score = 5
		return

	def firstCheck(self):
				#check to see if straight or flush
		self.isStraight()
		self.isFlush()
				#check to see if better flush
		if self.straight and self.flush:
			if self.values[0] == 0 and self.values[-1] == 12:
				self.score = 9
				return 
			else:
				self.score = 8
				return 

	def secondCheck(self):
				#check for all other possible hands

				#store high card regardless of score 
		if self.values[0] == 0:
			self.highCard = self.cards[0].getRank()
			self.highCardValue = self.cards[0].getValue()
			self.highCardSuit = self.cards[0].getSuit()
		else:
			self.highCard = self.cards[-1].getRank()
			self.highCardValue = self.cards[-1].getValue()
			self.highCardSuit = self.cards[-1].getSuit()
		
		if not (self.straight or self.flush):
			test_value = 0
			iterator = 0

			while iterator < (HANDSIZE - 1):
				value = self.values[iterator]
				count = 1
				for i in range(iterator, (HANDSIZE - 1), 1):
					if self.values[i] == self.values[i + 1]:
						count += 1
					else:
						break

				if count == 1:
					iterator += count
					continue 

				if self.score == 0:
					if count == 2:
						self.score = 1			#pair
					else:
						if count == 3:
							self.score = 3		#three of a kind
						else:
							if count == 4:		#four of a kind
								self.score = 7
				else:
					if self.score == 1 and count == 2:
						self.score = 2			#two pair
					else:
						if self.score == 1 and count == 3:
							self.score = 6		#full house
						else:
							if self.score == 3 and count == 2:
								self.score = 6	#full house
						
						#grab highest ranked card in score; in a full house: the three of a kind takes priority
						#store value of card for comparison; ace = 13
						# some DISCRETE MATH IN HERE!!!!! =]
						
				if self.cards[iterator].getValue() == 0:
					test_value = 13
				else:
					test_value = self.cards[iterator].getValue()

				if ((self.highRank == "") and (self.highRankValue < test_value)) or count == 3:
					self.highRank = self.cards[iterator].getRank()
					self.highRankValue = test_value
					self.highRankSuit = self.cards[iterator].getSuit()

					for i in range(1, count):
						if self.cards[iterator + i].getSuit() > self.highRankSuit:
							self.highRankSuit = self.cards[iterator + i].getSuit()
				else:
					if self.score == 2 and (self.highRankValue < test_value):
						self.highRank = self.cards[iterator].getRank()
						self.highRankValue = test_value
						self.highRankSuit = self.cards[iterator].getSuit()

						for i in range(1, count):
							if self.cards[iterator + i].getSuit() > self.highRankSuit:
								self.highRankSuit = self.cards[iterator + i].getSuit()
						

				iterator += count

		return
	
	def evaluateHand(self):
		if not self.evaluated:	
			self.firstCheck()
			self.secondCheck()

					#return for high card rank
			if self.score == 0:
				self.evaluated = True
				return "  %20sHigh Card: %5s" % ("", self.highCard)

					#return for highest rank if anything other than high card, straight, flush, SF or RF
			else:
				if self.highRank != "":
					self.evaluated = True  
					return "     %-17sBest Rank: %5s" % (SCORES[self.score], self.highRank)

					#return for straight, flush, SF or RF
			self.evaluated = True
			return "     %-17sHigh Card: %5s" % (SCORES[self.score], self.highCard)