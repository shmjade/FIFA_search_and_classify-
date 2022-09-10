import math
import csv
# =======================================================
# =============          FUNCTIONS        ===============
# =======================================================

# --------------------------------------------------
# -------------     general use    -----------------

# Returns a hash table with NUM_ENTRIES entries
def new_hash_table(NUM_ENTRIES):
	hash_table = []
	for i in range(0, NUM_ENTRIES):
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

# Opens the players.csv archive and inserts the players on the hash table of players
def read_players_csv(hash_players):
	with open("players.csv", "r") as archive:
		line_count = 0
		csv_table = csv.reader(archive, delimiter=",")
		i=0
		for row in csv_table:
			if(i!=0):
				hash_players = insert_hash_players(hash_players, (Player(int(row[0]), row[1], row[2], int(row[3]), int(row[4]), int(row[5]))))
			i+=1
	return hash_players


# --------------------------------------------------
# -------------     ratings.csv    -----------------

# Inserts a user in the users hash table, according to its user_id, and returns the hash table
def insert_hash_users(hash_users, a_user):
	hash_users[(a_user.getUserID())%NUM_ENTRIES_RATINGS].append(a_user)
	return hash_users

def insert_rating_player(hash_players, rating) #------------------------------> TERMINAR


def user_first_rating(hash_users, user_ID):  #------------------------------> TERMINAR
	# If there is no user on this hash entry, return 1 (this is the user's first rating)
	for user in hash_users[(user_ID)%NUM_ENTRIES_RATINGS]:
		if(user.getUserID()==user_ID):	# if a user has the ID of the user I'm searching
			return 0
	return 1


# Opens the rating.csv archive and inserts ... ---------> NOT FINISHED
def read_rating_csv(hash_users):
	with open("rating.csv", "r") as archive:
		line_count = 0
		csv_table = csv.reader(archive, delimiter=",")
		i=0
		for row in csv_table:
            new_user = User(row[0], [(row[1], row[2])])
			if(i!=0):
                # If this is the user's first rating, init the user and insert it:
                if(user_first_rating(hash_users, row[0])==1):
				    hash_users = insert_hash_users(hash_users, new_user)
                # If the user has already been inserted, only append this new rating:
                else:
                    hash_users[row[0]%NUM_ENTRIES_RATINGS].addRating((row[1], row[2]))
			i+=1
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