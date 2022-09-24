import math
from Functions.f_players import *


# --------------------------------------------------
# --------------    third search    ----------------

def search3(user_id, hash_users):
	print("----- PLAYERS REVIEWED BY USER " + str(user_id) + " -----")
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:12s}'.format("sofifa_id","name of the player", "global rating", "count", 'user rating'))
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:12s}'.format("sofifa_id","name of the player", "global rating", "count", 'user rating'))


def sort_rating(hash_users):
	print("oi")

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