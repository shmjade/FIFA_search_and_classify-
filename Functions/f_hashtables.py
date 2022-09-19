# =======================================================
# =============          FUNCTIONS        ===============
# =======================================================

# --------------------------------------------------
# -------------     general use    -----------------

# Returns a hash table with num entries
def new_hash_table(num):
	hash_table = []
	for i in range(0, num):
		hash_table.append([])
	return hash_table

# Prints the statistic of the given hash table
def statistic_entries(hash_table, NUM_ENTRIES):
	empty_entries = 0
	used_entries = 0
	longest = 0
	shortest = NUM_ENTRIES*NUM_ENTRIES

	for entry in hash_table:
		if(entry == []):
			shortest = 0
			empty_entries += 1
		else:
			used_entries += 1
			if(len(entry)>longest):
				longest = len(entry)
	print(" ======== STATISTIC =========")
	print("Number of empty entries: " + str(empty_entries))
	print("Number of used entries: " + str(used_entries))
	print("USED/TOTAL = " + str(used_entries/NUM_ENTRIES))
	print("Longest entries: " + str(longest))
	print("Shortest entries: " + str(shortest))
	
