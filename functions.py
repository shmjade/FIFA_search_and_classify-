''' O que falta:
1 - colocar a parte de positions -> read_players_csv
2 - colocar a parte de tags

'''
import math
import csv
from classes import *

# =======================================================
# =============          FUNCTIONS        ===============
# =======================================================

# --------------------------------------------------
# -------------     general use    -----------------

# Returns a hash table with num entries
def new_hash_table(num):
	hash_table = []
	for i in range(0, num):
		hash_table.append([])
	return hash_table

# Prints the statistic of the given hash table
def statistic_entries(hash_table, NUM_ENTRIES):
	empty_entries = 0
	used_entries = 0
	longest = 0
	shortest = NUM_ENTRIES*NUM_ENTRIES

	for entry in hash_table:
		if(entry == []):
			shortest = 0
			empty_entries += 1
		else:
			used_entries += 1
			if(len(entry)>longest):
				longest = len(entry)
	print(" ======== STATISTIC =========")
	print("Number of empty entries: " + str(empty_entries))
	print("Number of used entries: " + str(used_entries))
	print("USED/TOTAL = " + str(used_entries/NUM_ENTRIES))
	print("Longest entries: " + str(longest))
	print("Shortest entries: " + str(shortest))
	

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
	with open("players.csv", "r") as archive:
		line_count = 0
		csv_table = csv.reader(archive, delimiter=",")
		i=0
		for row in csv_table:
			if(i!=0):
				# Insert the player on the hash table
				hash_players = insert_hash_players(hash_players, (Player(int(row[0]), row[1], row[2], int(row[3]), int(row[4]), int(row[5]))))
				# Insert the name of the player on the Trie Tree
				root.insertTrie(row[1], row[0])     # row[1] is the name and row[0] is the sofifa_id
			i+=1
	return hash_players, root


# --------------------------------------------------
# -------------     ratings.csv    -----------------

# Inserts a user in the users hash table, according to its user_id, and returns the hash table
def insert_hash_users(hash_users, a_user):
	hash_users[(a_user.getUserID())%NUM_ENTRIES_RATINGS].append(a_user)
	return hash_users

def insert_rating_player(hash_players, rating): #------------------------------> rating = (sofifa_id, rating)
	# increment the rating count
	i = rating[0]%NUM_ENTRIES_PLAYERS
	j = find_player_index(hash_players, rating[0])
	(hash_players[i][j]).incCount()
	# Add the new rating and set the average
	(hash_players[i][j]).setAverage(rating[1])
	return hash_players


def user_first_rating(hash_users, user_ID):  #------------------------------> TERMINAR
	# If there is no user on this hash entry, return 1 (this is the user's first rating)
	for user in hash_users[(user_ID)%NUM_ENTRIES_RATINGS]:
		if(user.getUserID()==user_ID):	# if a user has the ID of the user I'm searching
			return 0
	return 1

#returns the index of the player on a entry of the players hash table
def find_player_index(hash_table, sofifa_id):
	i=0
	for player in hash_table[(sofifa_id)%NUM_ENTRIES_PLAYERS]:
		if(player.getSofifaID==sofifa_id):
			return i 
		i+=1
	return -1

#returns the index of the player on a entry of the players hash table
def find_user_index(hash_users, user_id):
	i=0
	for user in hash_users[(user_id)%NUM_ENTRIES_RATINGS]:
		if(user.getUserID==user_id):
			return i 
		i+=1
	return -1	# if the user is not on the list, return -1

# Opens the rating.csv file and:
# - inserts the user on the hash_users table;
# - updates the ratings of the players on hash_players
def read_rating_csv(hash_users, hash_players):
	with open("rating.csv", "r") as archive:
		line_count = 0
		csv_table = csv.reader(archive, delimiter=",")
		i=0
		count = 0
		for row in csv_table:
			if(i!=0):
				if(count==1000):
					print("OLOKO = ", i)
					count = 0
				rating = (int(row[1]), float(row[2]))	# row[1] is the sofifa_id and row[2] is the rating
				e = find_user_index(hash_users, int(row[0]))
				# If this is the user's first rating, init the user and insert it:
				if(e==-1):
					hash_users = insert_hash_users(hash_users, User(int(row[0]), rating))	# row[0] is the user_id

				# If the user has already been inserted, only append this new rating:
				else:
					j = int(row[0])%NUM_ENTRIES_RATINGS
					(hash_users[j][e]).addRating((int(row[1]), float(row[2])))
				# Update the player's rating:
				hash_players = insert_rating_player(hash_players, rating)
			i+=1
			count+=1
	return hash_users




# --------------------------------------------------
# -------------     positions    -------------------


def hash_pos(string):
	v=0
	for i in range(0,len(string)):
		v=v+math.ceil(pow(23, 3 - i - 1)*(1 + ord(string[i].lower())-97))
	v=v%47
	v=v%26
	return v

#List of positions used on the validation
#l =['GK','SW','RWB','LWB','RB','LB','CB','DM','RW','LW','LM','RM','CM','AM','CF','RF','LF','ST']
#results=[8, 5,  16,  17, 1, 2, 9, 18, 14, 15, 20, 19, 6, 3, 7, 25, 0, 4]

hash_table_position=new_hash_table(26)
for i in hash_players:
	for j in hash_player:
		if hash_player[i][j] is not None:
			str_pos= hash_player[i][j].getPosition()
			positions=str_pos.split(",")
			for p in positions:
				index=hash_pos(i)
				hash_table_position[index] ##insere ordenado