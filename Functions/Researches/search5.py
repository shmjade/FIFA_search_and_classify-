from Functions.f_players import * 
from Functions.Researches.search2 import *
from Classes.player import *
from math import *
import math

# Sorts a list of tuples (x, y) by the second value (y)
def quicksort5(list, opt, dir):
	if(len(list)>1):
		lower = []
		higher = []
		pivot = list.pop(math.floor(len(list)/2))
		for element in list:
			if(element[opt]<=pivot[opt]):	#orders by the given opt
				lower.append(element)
			else:
				higher.append(element)
		if(dir=='lower'):
			return quicksort5(lower,opt, dir) + [pivot] + quicksort5(higher,opt, dir)
		else:
			return quicksort5(higher,opt, dir) + [pivot] + quicksort5(lower,opt, dir)
	else:
		return list

# opt: 
# 0 - sofifa_id
# 1- imc  
# 2- weight
# 3- height
def search5(opt, dir, age1, age2, hash_age, hash_players):
	players  = []
	for i in range(age1, age2 +1):
		# hash_age objects are (sofifa_id, height, weight)
		for player in hash_age[i-16]:
			imc = float(player[2])/((float(player[1])*float(player[1]))/10000)
			players.append((int(player[0]),imc, float(player[2]), float(player[1])))
	players = quicksort5(players, opt, dir)
	print(' {:10s}'.format("sofifa_id"), end=" | ")
	print('{:49s}'.format("name"), end=" | ")
	print('age', end=" | ")
	print(' imc  ', end=" | ")
	print(' height ', end=" | ")
	print('weight', end=" | ")
	print('global_rating ')
	# players: (sofifa_id, imc, weight, height)
	i = 0
	while(i<20 and i<len(players)):
		printPlayer_5(hash_players, players[i][0], players[i][2], players[i][3], players[i][1])
		i+=1
