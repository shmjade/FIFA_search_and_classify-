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
from Functions.f_tags import *

# Opens the players.csv archive and:
# - inserts the players on the hash table of players
# - inserts the name of each player on the Trie Tree
def read_players_csv(hash_players, root, hash_age):
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
					max_position = len(row[2])				
				# Insert the player on the players hash table
				hash_players = insert_hash_players(hash_players, (Player(int(row[0]), row[1], row[2], int(row[3]), int(row[4]), int(row[5]))))
				# Insert the name of the player on the Trie Tree
				root.insertTrie(row[1], row[0])     # row[1] is the name and row[0] is the sofifa_id
				# Insert player on the age hash table
				# row[3] is the age and -16 because the youngest player is 16
				# row[4] is the height and row[5] is the weight
				# hash_age objects are (sofifa_id, height, weight)
				hash_age[int(row[3])-16].append((row[0], row[4], row[5]))
			i+=1
	print("========= MAX NAME = ", max_name)
	print("========= MAX POSITION = ", max_position)
	return hash_players, root, hash_age




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
			sofifa_id=int(row[1])
			rating=float(row[2])
			hash_users[int(row[0])].append((sofifa_id, rating))
			# Update the player's rating:
			hash_players = insert_rating_player(hash_players, (sofifa_id, rating))				
	return hash_users, hash_players



# Reads the tags.csv archive and returns a hash_tags hash table in which:
# - each tag is mapped into an entry according to the maping(word, M) function
# - 
def read_tags_csv(hash_tags):
	#archive=open("tags.csv", "r")
	with open("tags.csv", "r") as archive:
		line_count = 0
		csv_table = csv.reader(archive, delimiter=",")
		next(csv_table, None)  # skip the headers
		i=0
		for row in csv_table:
			if(i!=0):
				# Insert the tag on the hash table
				entry=hash_tags[maping(row[2].split(" ")[0], NUM_ENTRIES_TAGS)] #entry on the hash table
				j=0
				while(j<len(entry)): #while hasnt reached all elements in the hash entry
					if entry[j][0]==row[2]: #entry[j][0]=tag text
						entry[j].append(row[1]) #Apend the so_fifa id into the tag's list
						break #leave while loop
					j=j+1
				if j==len(entry):
					entry.append([row[2]])#Add a new tag on the list
					entry[j].append(row[1]) #Add the sofifa_id to the tag
			i+=1
	return hash_tags


