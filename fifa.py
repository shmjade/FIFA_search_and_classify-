import csv
import math
import definitions
import classes
import functions


# ==================================================================
# =====================      EXAMPLES       ========================
# ==================================================================

# ----- Players -----
# 1 - Creates a hash table for the players
hash_players = new_hash_table(NUM_ENTRIES_PLAYERS)
# 2 - Opens the players.csv archive and inserts the players on the hash table
read_players_csv(hash_players)
# 3 - Prints the statistic of the hash table
statistic_entries(hash_players, NUM_ENTRIES_PLAYERS)

# ----- Ratings -----
# 1 - Creates a hash table for the ratings (users)
hash_users = new_hash_table(NUM_ENTRIES_RATINGS)
# 2 - Opens the ratings.csv archive and inserts the ratings on the hash table
read_rating_csv(hash_players, hash_users)
# 3 - Prints the statistic of the hash table
statistic_entries(hash_users, NUM_ENTRIES_RATINGS)

# ----- Trie -----
root=TrieNode(-1," ")
root.insertTrie("Ana", 5)
root.insertTrie("astolfo", 10)
root.insertTrie("bia", 12)
root.printChildren(root,'')
root.searchPrefix("Ana")