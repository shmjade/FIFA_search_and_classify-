''' O que falta:
1 - colocar a parte de positions -> read_players_csv
2 - colocar a parte de tags
'''

import math
import csv
from unittest import skip
from Classes.player import *
from Classes.user import *
from Classes.trie_node import *
from Functions.f_users import *
from Functions.f_players import *
import time



# Opens the rating.csv file and:
# - inserts the user on the hash_users table;
# - updates the ratings of the players on hash_players
def read_rating_csv(hash_users, hash_players):
	with open("rating.csv", "r") as archive:
		line_count = 0
		csv_table = csv.reader(archive, delimiter=",")
		next(csv_table, None)  # skip the headers
		i=0
		start = time.time()
		for row in csv_table:
			rating = (int(row[1]), float(row[2]))	# row[1] is the sofifa_id and row[2] is the rating
			# If this is the user's first rating, init the user and insert it:
			if(hash_users[int(row[0])]==0):
				hash_users[int(row[0])] = User(int(row[0]), rating)	# row[0] is the user_id
			# If the user has already been inserted, only append this new rating:
			else:					
				hash_users[int(row[0])].addRating(rating)
			# Update the player's rating:
			hash_players = insert_rating_player(hash_players, rating)				
	end=time.time()
	print(end - start)
	#return hash_users, hash_players





