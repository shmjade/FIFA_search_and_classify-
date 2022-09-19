# --------------------------------------------------
# -------------     first search    -----------------

def search1(prefix, root, hash_players):
	print("----- PLAYERS THAT START WITH " + prefix + " -----")
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:7s}'.format("sofifa_id","name of the player", "positions", "rating", 'count'))
	found = root.searchPrefix(prefix)
	found.printChildren(found,prefix, hash_players)

# --------------------------------------------------
# -------------    second search    ----------------

def search2(user_id, hash_users):
	print("----- PLAYERS REVIEWED BY USER " + str(user_id) + " -----")
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:12s}'.format("sofifa_id","name of the player", "global rating", "count", 'user rating'))
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:12s}'.format("sofifa_id","name of the player", "global rating", "count", 'user rating'))


def sort_rating(hash_users):
	print("oi")
'''
2.2 According to the users
--> input: "user" + <USER ID>
--> output: a table with a maximum of 20 players reviewed by the user, ordered by the best ratings, with columns:
|   sofifa_id	|   name        |   global_rating       |	count         	|   user_rating        |
'''

# --------------------------------------------------
# --------------    third search    ----------------

def search3(user_id, hash_users, hash_players):
	print("----- PLAYERS REVIEWED BY USER " + str(user_id) + " -----")
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:12s}'.format("sofifa_id","name of the player", "global rating", "count", 'user rating'))
	print(' {:10s} | {:49s} | {:14s} | {:7s} | {:12s}'.format("sofifa_id","name of the player", "global rating", "count", 'user rating'))

# Prints the best (top 20) players review by the user
def best_by_user(user_id, hash_users, hash_players):
	
'''
2.3 Finding the best players of a given position
--> input: top<N> '<position>'
--> output: a table with the best <N> players of the position '<position>'
--> OBS: only players with a minimum of 1000 ratings are eligible 
|   sofifa_id	|   name        |   player_positions    |	rating      	|   count        |
'''