import math
from Functions.f_players import *
# --------------------------------------------------
# -------------     first search    -----------------

def search1(prefix, root, hash_players):
	print("----- PLAYERS THAT START WITH " + prefix + " -----")
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:7s}'.format("sofifa_id","name of the player", "positions", "rating", 'count'))
	found = root.searchPrefix(prefix)
	found.printChildren(found,prefix, hash_players)