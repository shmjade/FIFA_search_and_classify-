# --------------------------------------------------
# -------------        menu        -----------------
from Functions.researches import *
from definitions import NUM_ENTRIES_RATINGS
#[int] Prints the menu options, waits for the user input and return the user option
def menu(root, hash_players, hash_users):
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
		first_word = option.split()[0]
		opt = 1
		match first_word.lower():
			case 'player':
				search1(option.split()[1], root, hash_players)
				opt = 1
			case 'user':
				search2(int(option.split()[1]), hash_users, hash_players)
				opt = 2
			case 'top':
				opt = 3
			case 'tags':
				opt = 4
			case 'exit':
				opt = 5
			case default:
				print("INPUT NOT VALID")
				opt = 0
	return opt
		



