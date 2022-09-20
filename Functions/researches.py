import math
from Functions.f_players import *
# --------------------------------------------------
# -------------     first search    -----------------

def search1(prefix, root, hash_players):
	print("----- PLAYERS THAT START WITH " + prefix + " -----")
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:7s}'.format("sofifa_id","name of the player", "positions", "rating", 'count'))
	found = root.searchPrefix(prefix)
	found.printChildren(found,prefix, hash_players)

# --------------------------------------------------
# -------------    second search    ----------------

def search3(user_id, hash_users):
	print("----- PLAYERS REVIEWED BY USER " + str(user_id) + " -----")
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:12s}'.format("sofifa_id","name of the player", "global rating", "count", 'user rating'))
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:12s}'.format("sofifa_id","name of the player", "global rating", "count", 'user rating'))


def sort_rating(hash_users):
	print("oi")
'''
2.2 According to the users
--> input: "user" + <USER ID>
--> output: a table with a maximum of 20 players reviewed by the user, ordered by the best ratings, with columns:
|   sofifa_id	|   name        |   global_rating       |	count         	|   user_rating        |
'''

# --------------------------------------------------
# --------------    third search    ----------------

def search2(user_id, hash_users, hash_players):
	print("----- PLAYERS REVIEWED BY USER " + str(user_id) + " -----")
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:12s}'.format("sofifa_id","name of the player", "global rating", "count", 'user rating'))
	#Sorts the user ratings:
	sortered = quicksort(hash_users[user_id])
	print("len sortered = ", len(sortered))
	for i in range(0, 20):
		print("Sofifa_id = ", sortered[i][0])
		print("User rating = ",sortered[i][1])
		#printPlayer_2(hash_players, sortered[i][0], sortered[i][1])

# Prints the best (top 20) players review by the user
def quicksort(list):
	if(len(list)>1):
		lower = []
		higher = []
		pivot = list.pop(math.floor(len(list)/2))
		for element in list:
			if(element[1]<=pivot[1]):	#orders by the rating of the user
				lower.append(element)
			else:
				higher.append(element)
		return quicksort(lower) + [pivot] + quicksort(higher)
	else:
		return list
	
'''
2.3 Finding the best players of a given position
--> input: top<N> '<position>'
--> output: a table with the best <N> players of the position '<position>'
--> OBS: only players with a minimum of 1000 ratings are eligible 
|   sofifa_id	|   name        |   player_positions    |	rating      	|   count        |
'''