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
	sortered = quicksort2(hash_users[user_id])
	print("len sortered = ", len(sortered))
	if(len(sortered)>0):
		i=len(sortered)-1
		while(i>=0 and i>len(sortered)-21):
			printPlayer_2(hash_players, sortered[i][0], sortered[i][1])
			i-=1
	else:
		print("----- user "+user_id+"has no ratings -----")
# Prints the best (top 20) players review by the user
def quicksort2(list):
	if(len(list)>1):
		lower = []
		higher = []
		pivot = list.pop(math.floor(len(list)/2))
		for element in list:
			if(element[1]<=pivot[1]):	#orders by the rating of the user
				lower.append(element)
			else:
				higher.append(element)
		return quicksort2(lower) + [pivot] + quicksort2(higher)
	else:
		return list
	
'''
2.3 Finding the best players of a given position
--> input: top<N> '<position>'
--> output: a table with the best <N> players of the position '<position>'
--> OBS: only players with a minimum of 1000 ratings are eligible 
|   sofifa_id	|   name        |   player_positions    |	rating      	|   count        |
'''
def search3(position, N, hash_players, hash_positions):
	sortered = quicksort3(hash_positions[hash_pos(position)])
	i=len(sortered)-1
	while(i>=0 and i>len(sortered)-N-1):
		printPlayer_1(hash_players, sortered[i].getSofifaID())

	
def quicksort3(listPlayers):
	if(len(listPlayers)>1):
		lower = []
		higher = []
		pivot = listPlayers.pop(math.floor(len(listPlayers)/2))
		for player in listPlayers:
			if(player.getAverage()<=pivot.getAverage()):	#orders by the rating of the user
				lower.append(player)
			else:
				higher.append(player)
		return quicksort3(lower) + [pivot] + quicksort3(higher)
	else:
		return listPlayers