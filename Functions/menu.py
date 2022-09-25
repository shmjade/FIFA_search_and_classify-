# --------------------------------------------------
# -------------        menu        -----------------
from Functions.Researches.search1 import *
from Functions.Researches.search2 import *
from Functions.Researches.search3 import *
from Functions.Researches.search4 import *
from re import sub
 
from definitions import NUM_ENTRIES_RATINGS
#[int] Prints the menu options, waits for the user input and return the user option
def menu(root, hash_players, hash_users, hash_table_position):
	print("\t--- MENU ---")
	print("Options:")
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
				tags=option[5:].split("’")
				tags=[sub(r'[^a-zA-Z ]+', '', tag).strip() for tag in tags]
				#for i in range(0,len(tags)):
				#	tags[i]=sub(r'[^a-zA-Z ]+', '', tags[i])
				opt = 4
			case 'exit':
				opt = 5
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
		



