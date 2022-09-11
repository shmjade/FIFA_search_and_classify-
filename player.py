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
		self.rating_count = 0   # a contagem inicia como zero
		self.rating_avg = 0     # a média inicia como zero


	def incCount(self):
		# Incrementamos a contagem
		self.rating_count += 1
	
	def getSofifaID(self):
		return self.sofifa_id

	def getName(self):
		return self.name

	def getPosition(self):
		return self.position

	def getAverage(self):
		return self.rating_avg

	def getCount(self):
		return self.rating_count

	def setAverage(self, rating):
		# Multiplicamos a média anterior pela contagem anterior
		self.rating_avg = self.rating_avg*(self.rating_count-1)
		# Somamos a nova avaliação
		self.rating_avg += rating
		# Dividimos pela nova contagem e obtemos a média atualizada
		self.rating_avg = self.rating_avg/self.rating_count

	def __str__(self):
		return (str(self.sofifa_id) + " " + self.name + " " +  self.position + " " +  str(self.age) + " " +  str(self.height) + " " +  str(self.weight))


