import csv
from turtle import pos
from Classes.player import *
from Functions.f_positions import hash_pos
# --------------------------------------------------
# -------------     players.csv    -----------------

# Inserts a player in a hash table, according to its sofifa_id, and returns the hash table
def insert_hash_players(hash_players, a_player):
	hash_players[(a_player.getSofifaID())%NUM_ENTRIES_PLAYERS].append(a_player)
	return hash_players



# --------------------------------------------------
# -------------     ratings.csv    -----------------
def insert_rating_player(hash_players, rating): #------------------------------> rating = (sofifa_id, rating)
	# increment the rating count
	i = rating[0]%NUM_ENTRIES_PLAYERS
	j = find_player_index(hash_players, rating[0])
	# Add the new rating and set the average
	(hash_players[i][j]).addRating(rating[1])
	return hash_players

# --------------------------------------------------
# --------------     Researches    -----------------

#returns the index of the player on a entry of the players hash table
def find_player_index(hash_players, sofifa_id):
	i=0
	entry_index=(sofifa_id)%NUM_ENTRIES_PLAYERS
	for player in hash_players[entry_index]:
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
	print(' {:10s}'.format(str(player.getSofifaID())), end=" | ")
	print('{:49s}'.format(str(player.getName())), end=" | ")
	print('{:1.5f}       '.format(player.getAverage()), end=" | ")
	print('{:7s}'.format(str(player.getCount())), end=" | ")
	print('{:1.1f} '.format(user_rating))



