
# =======================================================
# ============          DEFINITIONS         =============
# =======================================================

# --------------------------------------------------
# --------------    Trie Tree    -------------------
ALPHABET_SIZE = 30


# --------------------------------------------------
# -------------     Hash tables    -----------------

# ----------- players.csv ----------
# Total number of players:
NUM_PLAYERS = 18944			# Number of rows on players.csv
# Number of entries on Players hash table
NUM_ENTRIES_PLAYERS = 9497  # --> closest prime number to NUM_PLAYERS

# ----------- rating.csv -----------
# Total number of ratings:
NUM_RATINGS = 1048576 			# Number of rows on ratings.csv
# Number of entries on Ratings hash table
NUM_ENTRIES_RATINGS = 524287 	# --> closest prime number to NUM_RATINGS

# ----------- tags.csv -----------



# -------------------------------------
'''
The ratings.csv file contains the columns:
|   user_id     |   sofifa_id   |   rating      |


The players.csv file contains the columns:
|   sofifa_id	|   name        |   player_positions    |	age	height_cm	|   weight_kg     |


The tags.csv file contains the columns:
|   user_id	    |   sofifa_id	|   tag         |


-------     Researches      --------
2.1 According to the players' names
--> input: a string "prefix"
--> output: a table with all players whose name start with the given string "prefix", containing the columns:
|   sofifa_id	|   name        |   player_positions    |	rating      	|   count        |

OBS: the rating and count fields were not given 
'''