# =======================================================
# =============            TO DO           ==============
# =======================================================
# Test: 
# - name prefix that is not listed: e.g. 'lalauo'
# - user that doesnt exist

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
# Number of player positions
NUM_POSITIONS = 26
# ----------- rating.csv -----------
# Total number of ratings:
NUM_RATINGS = 24188078 			# Number of rows on ratings.csv
# Number of entries on Ratings hash table
NUM_ENTRIES_RATINGS = 138494	# Number of users
# Number of user entries:
NUM_ENTRIES_USERS = 138494      # Number of users
# ----------- tags.csv -----------
NUM_TAGS = 936 			# Number of distinct tags
NUM_ENTRIES_TAGS = 463


# -------------------------------------
'''
****************************************************************************************************************************************************
*********            Files description            **************************************************************************************************
****************************************************************************************************************************************************

The ratings.csv file contains the columns:
|   user_id     |   sofifa_id   |   rating      |


The players.csv file contains the columns:
|   sofifa_id	|   name        |   player_positions    |	age	height_cm	|   weight_kg     |


The tags.csv file contains the columns:
|   user_id	    |   sofifa_id	|   tag         |


****************************************************************************************************************************************************
*********            Researches             ********************************************************************************************************
****************************************************************************************************************************************************

2.1 According to the players' names
--> input: "player" + '<prefix>'
--> output: a table with all players whose name start with the given string '<prefix>', containing the columns:
|   sofifa_id	|   name        |   player_positions    |	rating      	|   count        |

IMPLEMENTATION: 
--> To get the information, the steps are:
    1) finding the prefix
    2) finding all names of players that start with the prefix 
    3) when a player name is found, search for the player's information

-------------   STEPS 1 AND 2 -------------
--> To make the string searches faster, it was chosen to put the players' names on a Trie Tree in which the 
    indicator of the end of a word is:
    - the sofifa_id of the player if the letter is the end o a player's name
    - -1 if the letter is not the end of a player's name

-------------   STEP 3  -------------
--> The rating and count fields were not given on any file, so it was decided to create a class to store the data:
    --> name of the class: Player 
    --> fields:
		- sofifa_id 
		- name
		- position
		- age
		- height
		- weight
		- rating_count 
		- rating_sum 
--> To make the player's search faster, a hash table containing Player objects was created
    --> number of entries: NUM_ENTRIES_PLAYERS = 9497
    --> hash function: (a_player.getSofifaID())%NUM_ENTRIES_PLAYERS


2.2 According to the users
--> input: "user" + <USER ID>
--> output: a table with a maximum of 20 players reviewed by the user, ordered by the best ratings, with columns:
|   sofifa_id	|   name        |   global_rating       |	count         	|   user_rating        |

IMPLEMENTATION:
--> To get the information, the steps are:
    1) finding the user
    2) reading the list of ratings
    3) for each rating, finding the player's data:
    3.1) finding the player
    3.2) reading the player's information
    4) Order the list of players' ratings according to the highest ratings

-------------   STEP 2  -------------
--> To store each user's data, a new class was created:
    --> name of the class: User
    --> fields:    
		- ID				# the user ID
		- ratings			# a list of pairs (sofifa_id, rating) for each rating of the user
-------------   STEP 1  -------------
--> To make the user's search faster, a hash table containing User objects was created
    --> number of entries: NUM_ENTRIES_RATINGS = 524287
    --> hash function: (a_user.getUserID())%NUM_ENTRIES_RATINGS
-------------   STEP 3  -------------
--> To find and read the player's information, a search in the player's hash table is performed
-------------   STEP 4  -------------
--> To order the ratings, a sorting algorithm is used


**************************************************************************************************************************************************************************
** Se a classe não der certo, a alternativa dada pelo Comba é: criar uma outra tabela hash apenas com a contagem e média de avaliação dos jogadores

2.3 Finding the best players of a given position
--> input: top<N> '<position>'
--> output: a table with the best <N> players of the position '<position>'
--> OBS: only players with a minimum of 1000 ratings are eligible 
|   sofifa_id	|   name        |   player_positions    |	rating      	|   count        |

IMPLEMENTATION: 
--> To get the information, the steps are:
    --> Data structure 
    1) creating a list of positions, in which each position contains an list of sofifa_ids of the players
    1.1) create an empty list of positions
    2) while reading the players.csv file, inserting the sofifa_id of the players in each position
    2.1) to make the ranking easier, every time a player needs to be inserted, insert it ordered
    --> Search
    3) Map the position and return the list of the first <N> players of that position, as it is already ordered

2.4. According to players' tags 
--> input: tags <list of tags>
--> output: a table with all players that have the given list of tags
|   sofifa_id	|   name        |   player_positions    |	rating      	|   count        |
Example: tags ‘Brazil’ ‘Dribbler’


********************************************
*******         HASH TABLES         ********
********************************************
1) Players -> by sofifa_id
2) Positions -> by positions (INTEGER)
3) Users -> by user_id
4) Tags -> 

+++++++++ 1 Trie Tree

tabela[0] -> CM .... lista de sofifas



'''