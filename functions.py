''' O que falta:
1 - colocar a parte de positions -> read_players_csv
2 - colocar a parte de tags
'''

import math
import csv
import time
from unittest import skip
from Classes.player import *
from Classes.user import *
from Classes.trie_node import *
from Functions.f_users import *
from Functions.f_players import *


# Opens the rating.csv file and:
# - inserts the user on the hash_users table;
# - updates the ratings of the players on hash_players
'''
user_id	| sofifa_id	| rating
52505	| 158023	| 4
'''
def read_rating_csv(hash_users, hash_players):
	with open("rating.csv", "r") as archive:
		csv_table = csv.reader(archive, delimiter=",")
		next(csv_table, None)  # skip the headers
		for row in csv_table:
			# Insert the tuple (sofifa_id, rating) on the users' hash table:
			hash_users[int(row[0])].append((int(row[1]), float(row[2])))
			# Update the player's rating:
			hash_players = insert_rating_player(hash_players, (int(row[1]), float(row[2])))				
	return hash_users, hash_players





