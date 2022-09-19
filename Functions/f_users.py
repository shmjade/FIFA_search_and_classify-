import csv
# user_id is on range [1, 138493], so, we created a table with 138493 entries
# --------------------------------------------------
# -------------     ratings.csv    -----------------

#[hash table] Inserts a user in the users hash table, according to its user_id, and returns the hash table
def insert_hash_users(hash_users, user_id, rating):
	hash_users[user_id].append(rating)
	return hash_users


