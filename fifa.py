import csv
import math
import time
from definitions import *
from Classes.player import *
from Classes.user import *
from Classes.trie_node import *
from Functions.f_hashtables import *
from Functions.f_players import *
from Functions.f_positions import *
from Functions.f_tags import *
from Functions.f_users import *
from Functions.f_archives import *
from Functions.menu import *



# ==================================================================
# =====================      EXAMPLES       ========================
# ==================================================================

# ----- Players -----
# 0 - Creates a hash table for the players and a table for the positions
hash_players = new_hash_table(NUM_ENTRIES_PLAYERS)
hash_positions = new_hash_table(NUM_POSITIONS)
# 1 - Creates a Trie Tree for the players' names
root=TrieNode(-1," ")


# 2 - Opens the players.csv archive and inserts the players on the hash table
start = time.time()
hash_players, root = read_players_csv(hash_players, root)
end = time.time()

# 3 - Prints the statistic of the hash table
print(" ------- PLAYERS HASH TABLE -------")
print("Load time = "+ str(end-start))
print(" ------- END PLAYERS -------")
statistic_entries(hash_players, NUM_ENTRIES_PLAYERS)


# ----- Ratings -----
# 1 - Creates a hash table for the ratings (users)
hash_users = new_hash_table(NUM_ENTRIES_USERS)


# 2 - Opens the ratings.csv archive and inserts the ratings on the hash table
print(" ------- USERS HASH TABLE -------")
start = time.time()
hash_users, hash_players = read_rating_csv(hash_users, hash_players)
end = time.time()
print(" ------- END USERS -------")
# 3 - Prints the statistic of the hash table
print("Load time = "+ str(end-start))
statistic_entries(hash_users, NUM_ENTRIES_RATINGS)

# ----- Trie ----

# 4 - Add the players in sorted lists for their positions
print(" ------- POSITIONS HASH TABLE -------")
start = time.time()
hash_table_position=map_positions(hash_players)
end = time.time()
print(" ------- END POSITIONS -------")
# 4 - Prints the statistic of the hash table
print("Load time = "+ str(end-start))
statistic_entries(hash_table_position, 26)


#-----   Tags   -----
# 1 - Creates a hash table for the tags
hash_tags = new_hash_table(NUM_ENTRIES_TAGS)

# 2 - Opens the tags.csv archive and inserts the ratings on the hash table
print(" ------- TAGS HASH TABLE -------")
start = time.time()
hash_tags = read_tags_csv(hash_tags)
end = time.time()
print("Load time = "+ str(end-start))
print(" ------- END TAGS -------")

#-----   Menu   -----
flag_menu=0
while(flag_menu!=5):
    flag_menu = menu(root, hash_players, hash_users)


