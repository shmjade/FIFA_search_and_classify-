# --------------------------------------------------
# -------------        menu        -----------------
from Functions.Researches.search1 import *
from Functions.Researches.search2 import *
from Functions.Researches.search3 import *
from Functions.Researches.search4 import *
from Functions.Researches.search5 import *
from re import sub
 
from definitions import NUM_ENTRIES_RATINGS
#[int] Prints the menu options, waits for the user input and return the user option
def menu(root, hash_players, hash_users, hash_table_position, hash_tags, hash_age):
	print("\t--- MENU ---")
	print("    Options:")
	print("player <prefix of the names>")
	print("user <user ID>")
	print("top<number of players> <position>")
	print("tags <list of tags>")
	print("exit")
	opt = 0
	while(opt==0):
		option = input("Type your search: ")
		words = option.split()		
		opt = 1
		match words[0].lower():
			case 'player':
				search1(option.split(' ',1)[1], root, hash_players)
				opt = 1
			case 'user':
				search2(int(words[1]), hash_users, hash_players)
				opt = 2			
			case 'tags':
				# Get the tags list
				tags=option[5:]
				list_tags = []
				i=0
				while(i<len(tags)):
					#Find the first '
					while(i<len(tags) and tags[i]!="‘"):
						i+=1
					i+=1
					word = ""
					#Append all letters until the next ' is found
					while(i<len(tags) and tags[i]!="’"):
						word = word + tags[i]
						i+=1
					#Append the word to the list of tags
					list_tags.append(word)
					i+=1
				# Search for the players of the given tags
				search4(list_tags, hash_tags, hash_players)
				opt = 4
			case 'exit':
				opt = 5
			case 'age':
				opt=6
				feature = opt_search5(words[3])
				if(feature!=-1):
					search5(feature, words[2], int(words[1]), hash_age, hash_players)
				else:
					print("INVALID INPUT")
			case default: 
				if words[0].lower()[:3]=='top':
					#1st-List comprehension to clear all chars than letters
					#2nd-Convert to int the following to top
					#3th-The list of positions ordered by players' scores
					search3("".join(c for c in words[1] if c.isalpha()),int(words[0][3:]), hash_table_position)
					opt = 3
				else:
					print("INPUT NOT VALID")
					opt = 0
	return opt
		



