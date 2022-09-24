import math
from Functions.f_hashtables import new_hash_table
# --------------------------------------------------
# -----------     player positions    --------------

#[int] Maps the string (player's position) into a number that will be the table index (entry)
# OBS: all positions have a different index with this hash function
#l =['GK','SW'	,'RWB','LWB','RB','LB',	'CB','DM','RW','LW','LM','RM','CM','AM','CF','RF','LF','ST']
#i =[	8,	5	, 	16,	  17, 	1, 	 2,	   9,  18,  14,  15,  20,  19,	 6,	  3,   7,  25,	 0, 4]
def hash_pos(string):
	v=0
	for i in range(0,len(string)):
		v=v+math.ceil(pow(23, 3 - i - 1)*(1 + ord(string[i].lower())-97))
	v=v%47
	v=v%26
	return v

#Inserts the player on the hash table according to it's position in a sorted way, because 
#the researches are ranked (best first)
#Implementation based on https://www.geeksforgeeks.org/python-program-for-binary-insertion-sort/
#Receives a list of players (one for each position), one player, and one start and ending position
#To start the recursive sorted insertion, the list should be full, the start should be 0 and end the last index of the list
def player_sorted_insertion(list, player, start, end):	
	if start==end: #Found the position
		if list[start].getAverage()>player.getAverage():
			return start #insert on the left
		else:
			return start+1 #Insert on the right
	if start>end:
		return start 
	mid=(start+end)//2  # integer division uses //
	if list[mid].getAverage() < player.getAverage():
		return player_sorted_insertion(list, player, mid+1, end)
	elif list[mid].getAverage() > player.getAverage():
		return player_sorted_insertion(list, player, start, mid-1)
	else:
		return mid


#[sorting algorithm] After all ratings are read and the players are updated
#sort the players on the hash table of positions to make the researches
#Receive the hash table of player and return the list of positions ordered by ranking
def map_positions(hash_players):
	hash_table_position=new_hash_table(26)
	for entry in hash_players:
		for p in entry:	
			if(p.getCount()>1000): #Add on the positions ranking only those players who have +1000 evaluations
				str_pos=p.getPosition()
				positions=str_pos.split(", ")
				for pos in positions:
					index=hash_pos(pos)
					if len(hash_table_position[index])==0:
						hash_table_position[index].append(p)
					else:
						pos=player_sorted_insertion(hash_table_position[index],p,0,len(hash_table_position[index])-1)
						hash_table_position[index]=hash_table_position[index][:pos]+[p]+hash_table_position[index][pos:]
	return hash_table_position
