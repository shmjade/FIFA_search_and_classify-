import math
from Functions.Researches.search2 import quicksort2
from Functions.f_players import *
from Functions.f_tags import maping

# --------------------------- Tags search 
'''
2.4. According to players' tags 
--> input: tags <list of tags>
--> output: a table with all players that have the given list of tags
|   sofifa_id	|   name        |   player_positions    |	rating      	|   count        |
Example: tags ‘Brazil’ ‘Dribbler’
'''

# Receives two lists of sofifa_ids and return a list of the intersection of them
def intersection(list1, list2):
	intersec = []
	for sofifa1 in list1:
		for sofifa2 in list2:
			if sofifa1==sofifa2:
				intersec.append(sofifa1)
	return intersec

# Returns the lists of lists of sofifa_ids ordered by the length of the lists
def sort_lists(lists):
	size_lists = []
	for i in range(0, len(lists)):
		size_lists.append([i, len(lists[i])])
	size_lists = quicksort2(size_lists)
	ordered = []
	for i in range(0, len(lists)):
		ordered.append(lists[size_lists[i][0]])
	return ordered
	
# Receives a list and returns the list without duplicate elements			
def remove_duplicates(a_list):
	new = []
	for element1 in a_list:
		insert = 1
		for element2 in new:
			if element1==element2:
				insert=0
		if insert==1:
			new.append(element1)
	return new

# Receives a tag and returns the list of sofifa_ids of the players that have this tag
def get_list_tags(tag, hash_tags):
	list = []
	entry_lists=hash_tags[maping(tag.split(" ")[0], NUM_ENTRIES_TAGS)]
	for entry in entry_lists:
		if(entry[0]==tag):
			list = remove_duplicates(entry[1:])	
	return list 


# Receives the tags_list list, the hash_tags and hash_players tables and prints
# the players that have all of the tags on the given list of tags
def search4(tags_list, hash_tags, hash_players):
	if(len(tags_list)==0):
		print("Warning: empty list of tags")
		return -1
	else:
		# Get the first list of sofifa_ids
		intersec = get_list_tags(tags_list[0], hash_tags)
		# Get the intersection with the other lists
		i=1
		while(i<len(tags_list)):
			intersec = intersection(intersec, get_list_tags(tags_list[i], hash_tags))
			i+=1
		# Print the players
		print("----- PLAYERS OF THE TAGS -----")
		if(intersec==[]):
			print("No player has all tags given")
		else:
			print(' {:10s} | {:49s} | {:14s} | {:7s} | {:7s}'.format("sofifa_id","name of the player", "positions", "rating", 'count'))
			for sofifa_id in intersec:
				printPlayer_1(hash_players, int(sofifa_id))
	





	