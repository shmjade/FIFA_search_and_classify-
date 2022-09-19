import csv
from Classes.player import *
# --------------------------------------------------
# -------------     players.csv    -----------------

# Inserts a player in a hash table, according to its sofifa_id, and returns the hash table
def insert_hash_players(hash_players, a_player):
	hash_players[(a_player.getSofifaID())%NUM_ENTRIES_PLAYERS].append(a_player)
	return hash_players

# Opens the players.csv archive and:
# - inserts the players on the hash table of players
# - inserts the name of each player on the Trie Tree
def read_players_csv(hash_players, root):
	max_name = 0
	max_position = 0

	with open("players.csv", "r") as archive:
		line_count = 0
		csv_table = csv.reader(archive, delimiter=",")
		i=0
		for row in csv_table:
			if(i!=0):
				if(len(row[1])>max_name):
					max_name = len(row[1])
				if(len(row[2])>max_position):
					max_position = len(row[2])				# Insert the player on the hash table
				hash_players = insert_hash_players(hash_players, (Player(int(row[0]), row[1], row[2], int(row[3]), int(row[4]), int(row[5]))))
				# Insert the name of the player on the Trie Tree
				root.insertTrie(row[1], row[0])     # row[1] is the name and row[0] is the sofifa_id
			i+=1
	print("========= MAX NAME = ", max_name)
	print("========= MAX POSITION = ", max_position)
	return hash_players, root

# --------------------------------------------------
# -------------     ratings.csv    -----------------
def insert_rating_player(hash_players, rating): #------------------------------> rating = (sofifa_id, rating)
	# increment the rating count
	i = rating[0]%NUM_ENTRIES_PLAYERS
	j = find_player_index(hash_players, rating[0])
	(hash_players[i][j]).incCount()
	# Add the new rating and set the average
	(hash_players[i][j]).sumAverage(rating[1])
	return hash_players

# --------------------------------------------------
# --------------     Researches    -----------------

#returns the index of the player on a entry of the players hash table
def find_player_index(hash_players, sofifa_id):
	i=0
	for player in hash_players[(sofifa_id)%NUM_ENTRIES_PLAYERS]:
		if(player.getSofifaID()==sofifa_id):
			return i 
		i+=1
	return -1

# Prints the player's information on the following configuration:
# |   sofifa_id	|   name        |   player_positions    |	rating      	|   count        |
def printPlayer_1(hash_players, sofifa_id):
	i = sofifa_id%NUM_ENTRIES_PLAYERS
	j = find_player_index(hash_players, sofifa_id)
	player = hash_players[i][j]
	print(' {:10s} | {:49s} | {:14s} |  {:1.2f}   | {:6d}'.format(str(player.getSofifaID()), str(player.getName()), player.getPosition(), player.getAverage(), player.getCount()))

# Prints the player's information on the following configuration:
# |   sofifa_id	|   name        |   global_rating       |	count         	|   user_rating        |
def printPlayer_2(hash_players, sofifa_id, user_rating):
	i = sofifa_id%NUM_ENTRIES_PLAYERS
	j = find_player_index(hash_players, sofifa_id)
	player = hash_players[i][j]
	print(str(player.getSofifaID()), end=" | ")
	print('{:49s} | {:1.2f} | {:6d} | {:1.1f}'.format(str(player.getName()), player.getAverage(), player.getCount()), user_rating)




