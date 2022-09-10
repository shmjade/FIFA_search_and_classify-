import csv
import math
from definitions import *
from player import *
from user import *
from trie_node import *
from functions import *


# ==================================================================
# =====================      EXAMPLES       ========================
# ==================================================================

# ----- Players -----
# 0 - Creates a hash table for the players and a table for the positions
hash_players = new_hash_table(NUM_ENTRIES_PLAYERS)

# 1 - Creates a Trie Tree for the players' names
root=TrieNode(-1," ")


# 2 - Opens the players.csv archive and inserts the players on the hash table
hash_players, root = read_players_csv(hash_players, root)

# 3 - Prints the statistic of the hash table
print(" ------- PLAYERS HASH TABLE -------")
statistic_entries(hash_players, NUM_ENTRIES_PLAYERS)


# ----- Ratings -----
# 1 - Creates a hash table for the ratings (users)
hash_users = new_hash_table(NUM_ENTRIES_RATINGS)

# 2 - Opens the ratings.csv archive and inserts the ratings on the hash table
print(" ------- USERS HASH TABLE -------")
read_rating_csv(hash_users, hash_players)
print(" ------- END -------")
# 3 - Prints the statistic of the hash table
statistic_entries(hash_users, NUM_ENTRIES_RATINGS)

# ----- Trie -----
root=TrieNode(-1," ")
root.insertTrie("Ana", 5)
root.insertTrie("astolfo", 10)
root.insertTrie("bia", 12)
root.printChildren(root,'')
root.searchPrefix("Ana")