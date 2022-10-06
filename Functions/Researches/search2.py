import math
from Functions.f_players import *

'''
2.2 According to the users
--> input: "user" + <USER ID>
--> output: a table with a maximum of 20 players reviewed by the user, ordered by the best ratings, with columns:
|   sofifa_id	|   name        |   global_rating       |	count         	|   user_rating        |
'''

# --------------------------------------------------
# --------------    second search    ---------------

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
		print("----- user "+str(user_id)+" has no ratings -----")

# Sorts a list of tuples (x, y) by the second value (y)
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
	