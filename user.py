from definitions import *
# =======================================================
# ==============          CLASSES        ================
# =======================================================

# -----------------------------------------------
# --------------      User      -----------------
class User:
	def __init__(self, ID, ratings):
		self.ID = ID				# the user ID - integer
		self.ratings = []			# a list of pairs (sofifa_id, rating) for each rating of the user -> both integers
		self.ratings.append(ratings)
	def getUserID(self):
		return self.ID
	def addRating(self, rating):
		self.ratings.append(rating)
	def getRatings(self):
		return self.ratings

