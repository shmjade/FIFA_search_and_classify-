import math
from Functions.f_players import *
from Functions.f_positions import *


# --------------------------------------------------
# --------------    third search    ----------------
'''
2.3 Finding the best players of a given position
--> input: top<N> '<position>'
--> output: a table with the best <N> players of the position '<position>'
--> OBS: only players with a minimum of 1000 ratings are eligible 
|   sofifa_id	|   name        |   player_positions    |	rating      	|   count        |
'''


def search3(position, N, hash_table_position):
	print("----- PLAYERS OF POSITION " + str(position) + " -----")
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:6s}'.format("sofifa_id","name of the player", "position", "rating", 'count'))
	position_index=hash_pos(position)
	position_list=hash_table_position[position_index][len(hash_table_position[position_index])-N:]
	for i in range(len(position_list)-1,-1,-1): #Pass though the list on the invert the order
		player=position_list[i]
		print(' {:10s} | {:49s} | {:14s} |  {:1.2f}   | {:6d}'.format(str(player.getSofifaID()), str(player.getName()), player.getPosition(), player.getAverage(), player.getCount()))
	

