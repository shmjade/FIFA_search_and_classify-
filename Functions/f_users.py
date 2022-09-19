import csv
# user_id is on range [1, 138493], so, we created a table with 138493 entries
# --------------------------------------------------
# -------------     ratings.csv    -----------------

# Inserts a user in the users hash table, according to its user_id, and returns the hash table
def insert_hash_users(hash_users, a_user):
	hash_users[(a_user.getUserID())%NUM_ENTRIES_RATINGS].append(a_user)
	return hash_users




# [boolean] Returns 1 if it is the user's first rating or 0 if it is not
def user_first_rating(hash_users, user_ID):  #------------------------------> TERMINAR
	# If there is no user on this hash entry, return 1 (this is the user's first rating)
	for user in hash_users[(user_ID)%NUM_ENTRIES_RATINGS]:
		if(user.getUserID()==user_ID):	# if a user has the ID of the user I'm searching
			return 0
	return 1

# [int] Returns the index of the user on a entry of the users hash table 
# (returns -1 if it's not inserted on the hash table)
def find_user_index(hash_users, user_id):
	i=0
	for user in hash_users[(user_id)%NUM_ENTRIES_RATINGS]:
		if(user.getUserID==user_id):
			return i 
		i+=1
	return -1	# if the user is not on the list, return -1
