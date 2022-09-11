from definitions import *
from functions import *

# =======================================================
# ==============          CLASSES        ================
# =======================================================
# -----------------------------------------------
# -------------    Trie Node    -----------------
class TrieNode:
	def __init__(self, EndOfWord, letter):
		# EndOfWord is -1 if the letter does not represent the end of a word. Otherwise, its
		# value represents the sofifa_id of the player whose name is the word represented
		self.EndOfWord = EndOfWord 
		self.children = [None]*ALPHABET_SIZE
		self.letter = letter

	def getEndOfWord(self):
		return self.EndOfWord
	
	# Searches for a Player in the Trie Tree and returns:
	# - the sofifa_id of a Player if he was found
	def searchPrefix(self, word):
		# the node is where we search for the letter word[w] in node's children
		node = self
		size = len(word)        # the length of the word that we are searching for
		w = 0           # index for the word
		c = 0           # index for the children
		word=word.lower()
		while(w<size):           # outer loop --------> searchs for all letters
			# Checks if one the children has the letter searched:
			while(c<len(node.children)):
				if(node.children[c] is None):
					c+=1
				elif node.children[c].letter==word[w]:
					break
				else:
					c+=1
			# Checks if the it ran out of children and returns -1 if so 
			if(c==len(node.children)):
				return -1
			# If it didn't go out of children, it found the letter
			else:
				w += 1                          # will search for the next letter
				node = node.children[c]         # updates the node 
				c = 0                           # resets the first child
		return node   # Returns the sofifa_id if the letter is the end of a word or -1 if it is not

	def insertTrie(self, key, code):
		current=self
		for i in range(0,len(key)):
			l=key[i].lower()
			index=ord(l)-97
			if index<0 or index>26:	
				#No a-z characters ordered by frequency
				if index==-65: #' ' character
					index=29 
				elif index==-52: #'-' character
					index=27 
				elif index==-58: #"'" character
					index=28 
				elif index==-51: #'.' character
					index=26
				else:
					index=29
			if(current.children[index] is None):
				if(i==len(key)):
					novo=TrieNode(code, l)
					current.children[index]=novo
				else:
					novo=TrieNode(-1, l)
					current.children[index]=novo
			if(i==len(key)-1):
				current.children[index].EndOfWord=int(code)
			current=current.children[index]

	def printChildren(self, node, string, hash_players):
		string=string+node.letter
		if node==None:
			return 
		total=len(node.children)
		for i in range(0, total-1):
			if node.children[i] is not None:
				self.printChildren(node.children[i], string, hash_players)
		if node.EndOfWord!=-1:
			#print("end of word/sofifa = ",node.EndOfWord)
			printPlayer_1(hash_players, node.getEndOfWord())
			#print("Sofifa = ", hash_players[node.getEndOfWord()%NUM_ENTRIES_PLAYERS][find_player_index(hash_players, node.getEndOfWord())].getSofifaID())
			#print("Name = " + (hash_players[node.getEndOfWord()%NUM_ENTRIES_PLAYERS][find_player_index(hash_players, node.getEndOfWord())]).getName())
		if node.children[total-1] is not None:
			self.printChildren(node.children[total-1], string, hash_players)



