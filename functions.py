''' O que falta:
1 - colocar a parte de positions -> read_players_csv
2 - colocar a parte de tags

'''
import math
import csv
from unittest import skip
from player import *
from user import *
from trie_node import *
import time

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
	

# Map a string into a hash value from 0 e M−1:
# F(string) = (string[0]*3^0 + string[1]*3^1 + ... + string[n-2]*3^(n-2) + string[n-1]*3^(n-1))%M
def maping(word, M):
    sum=0
    for i in range(0,len(word)):
        sum += ord(word[i].lower())*math.pow(3,i)
    return math.floor(int(sum))%M


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

def printPlayer_1(hash_players, sofifa_id):
	i = sofifa_id%NUM_ENTRIES_PLAYERS
	j = find_player_index(hash_players, sofifa_id)
	player = hash_players[i][j]
	print(str(player.getSofifaID()), end="")
	print(" | " + str(player.getName()), end="")
	print(" | " + str(player.getPosition()), end="")
	print(" | " + str(player.getAverage()))

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
def find_player_index(hash_players, sofifa_id):
	i=0
	for player in hash_players[(sofifa_id)%NUM_ENTRIES_PLAYERS]:
		#print("sofifa = ", player.getSofifaID())
		#print("name = " + player.getName())
		#print("i = ", i)
		if(player.getSofifaID()==sofifa_id):
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
		next(csv_table, None)  # skip the headers
		i=0
		start = time.time()
		for row in csv_table:
			if(i!=0):
				if(i%1000000==0):
					print("Ratings = ", i)
					end=time.time()
					print(end - start)
					start=end
				rating = (int(row[1]), float(row[2]))	# row[1] is the sofifa_id and row[2] is the rating
				# If this is the user's first rating, init the user and insert it:
				if(hash_users[int(row[0])]==0):
					hash_users[int(row[0])] = User(int(row[0]), rating)	# row[0] is the user_id
				# If the user has already been inserted, only append this new rating:
				else:					
					hash_users[int(row[0])].addRating(rating)
				# Update the player's rating:
				hash_players = insert_rating_player(hash_players, rating)				
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

#Implementation based on https://www.geeksforgeeks.org/python-program-for-binary-insertion-sort/
def player_sorted_insertion(list, player, start, end):	
	if start==end: #Found the position
		if list[start].getAverage()>player.getAverage():
			return start #insert on the left
		else:
			return start+1 #Insert on the right
	if start>end:
		return start 
	mid=(start+end)//2
	if list[mid].getAverage() < player.getAverage():
		return player_sorted_insertion(list, player, mid+1, end)
	elif list[mid].getAverage() > player.getAverage():
		return player_sorted_insertion(list, player, start, mid-1)
	else:
		return mid


#List of positions used on the validation
#l =['GK','SW','RWB','LWB','RB','LB','CB','DM','RW','LW','LM','RM','CM','AM','CF','RF','LF','ST']
#results=[8, 5,  16,  17, 1, 2, 9, 18, 14, 15, 20, 19, 6, 3, 7, 25, 0, 4]

def map_positions(hash_players):
	hash_table_position=new_hash_table(26)
	for entry in hash_players:
		for p in entry:			
			str_pos=p.getPosition()
			positions=str_pos.split(",")
			for pos in positions:
				index=hash_pos(pos)
				if len(hash_table_position[index])==0:
					hash_table_position[index].append(p)
				else:
					pos=player_sorted_insertion(hash_table_position[index],p,0,len(hash_table_position[index])-1)
					hash_table_position[index]=hash_table_position[index][:pos]+[p]+hash_table_position[index][pos:]
	return hash_table_position


# ===================  Tags  ===================
def tags_sorted_insertion(list, sofifa_id, start, end):	
	if start==end: #Found the position
		if list[start]==sofifa_id:
			return 0
		elif list[start]>sofifa_id:
			return start #insert on the left
		else:
			return start+1 #Insert on the right
	if start>end:
		return start 
	mid=(start+end)//2
	if list[mid] < sofifa_id:
		return tags_sorted_insertion(list, sofifa_id, mid+1, end)
	elif list[mid] > sofifa_id:
		return tags_sorted_insertion(list, sofifa_id, start, mid-1)
	else:
		return mid

def read_tags_csv(hash_tags):
	with open("tags.csv", "r") as archive:
		line_count = 0
		csv_table = csv.reader(archive, delimiter=",")
		next(csv_table, None)  # skip the headers
		i=0
		start=time.time()
		for row in csv_table:
			if(i%100==0):
					print("Tags = ", i)
					end=time.time()
					print(end - start)
					start=end
			if(i!=0):
				# Insert the tag on the hash table
				entry=hash_tags[maping(row[2].split(" "), NUM_ENTRIES_TAGS)] #entry on the hash table
				j=0
				while(j<len(entry)): #while hasnt reached all elements in the hash entry
					if entry[j][0]==row[2]: #entry[j][0]=tag text
						entry[j].append(row[1]) #Apend the so_fifa id into the tag's list
						break #leave while loop
				if j==len(entry):
					entry.append([row[2]])#Add a new tag on the list
					entry[j].append(row[1]) #Add the sofifa_id to the tag
			i+=1
	return hash_tags
