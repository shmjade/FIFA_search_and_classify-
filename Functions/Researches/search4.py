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
		print(lists[size_lists[i][0]])
	return ordered
	
# Receives the tags_list list, the hash_tags and hash_players tables and prints
# the players that have all of the tags on the given list of tags
def search4(tags_list, hash_tags, hash_players):
	print("----- PLAYERS OF THE TAGS -----")
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:7s}'.format("sofifa_id","name of the player", "positions", "rating", 'count'))
	if(len(tags_list)>1):
		# Gets the lists of lists of sofifa_ids according to the tags
		lists = []
		# For each tag of the list of tags
		for tag in tags_list:
			# Gets the list of list of sofifa_ids on the hash_tags table, according to the tag
			entry_lists=hash_tags[maping(tag, NUM_ENTRIES_TAGS)]
			# Only insert the list of sofifa_ids that concerns the given tag:
			for minor_list in entry_lists:
				print(minor_list[0])
				# Verify if the element0 is the given tag:
				if minor_list[0]==tag:
					# If so, append the list of sofifa_ids without the first element (tag) and the duplicates
					lists.append(remove_duplicates(minor_list[1:]))
		# Order the lists of lists of sofifa_ids by the length of the lists
		lists = sort_lists(lists)
		# Get the intersection of the lists:
		intersec = intersection(lists[0], lists[1])
		for i in range(2, len(tags_list)):
			intersec = intersection(intersec, lists[i])
	else:
		entry_lists = hash_tags[maping(tags_list[0], NUM_ENTRIES_TAGS)]
		for minor_list in entry_lists:
			if minor_list[0]==tags_list[0]:
				intersec = remove_duplicates(minor_list[1:])
	#print("---- intersec ----")
	#print(intersec)
	for sofifa_id in intersec:
		printPlayer_1(hash_players, int(sofifa_id))
	
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




	