from definitions import *
# -----------------------------------------------
# --------------     Player     -----------------
class Player:
	def __init__(self, sofifa_id, name, position, age, height, weight): 
		self.sofifa_id = sofifa_id 
		self.name = name
		self.position = position
		self.age = age
		self.height = height
		self.weight = weight
		self.rating_count = 0   # the count starts as zero
		self.rating_sum = 0     # the average starts as zero
		self.index = 0			# the index inside the hash_players entry list

	def incCount(self):
		# Increments the count
		self.rating_count += 1
	
	def getSofifaID(self):
		return self.sofifa_id

	def getName(self):
			return self.name

	def getPosition(self):
		return self.position

	def getAverage(self):
		try:
			m = self.rating_sum/self.rating_count
		except ZeroDivisionError:
			m = 0
		return m

	def getCount(self):
		return self.rating_count

	# The rating_sum atribute is, when the ratings are being 
	# read, the sum of the ratings
	def addRating(self, rating):
		self.rating_sum = self.rating_sum + rating
		self.rating_count =self.rating_count+ 1

	
	# The rating_sum atribute only represents the average when 
	# a research is made -- DEPRECATED
	#def setAverage(self, rating):
	#	self.rating_sum = self.rating_sum/self.rating_count

	def __str__(self):
		return (str(self.sofifa_id) + " " + self.name + " " +  self.position + " " +  str(self.age) + " " +  str(self.height) + " " +  str(self.weight))


