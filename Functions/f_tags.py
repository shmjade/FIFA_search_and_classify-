import csv
from definitions import *
import math 
# ===================  Tags  ===================

# Maps a string into a hash value from 0 e M−1:
# F(string) = (string[0]*3^0 + string[1]*3^1 + ... + string[n-2]*3^(n-2) + string[n-1]*3^(n-1))%M
def maping(word, M):
    sum=0
    for i in range(0,len(word)):
        sum += ord(word[i].lower())*math.pow(3,i)
    return math.floor(int(sum))%M


def tags_sorted_insertion(list, sofifa_id, start, end):	
	if start==end: #Found the position
		if list[start]==sofifa_id:
			return 0
		elif list[start]>sofifa_id:
			return start #insert on the left
		else:
			return start+1 #Insert on the right
	if start>end:
		return start 
	mid=(start+end)//2
	if list[mid] < sofifa_id:
		return tags_sorted_insertion(list, sofifa_id, mid+1, end)
	elif list[mid] > sofifa_id:
		return tags_sorted_insertion(list, sofifa_id, start, mid-1)
	else:
		return mid

# Reads the tags.csv archive and returns a hash_tags hash table in which:
# - each tag is mapped into an entry according to the maping(word, M) function
# - 
def read_tags_csv(hash_tags):
	#archive=open("tags.csv", "r")
	with open("tags.csv", "r") as archive:
		line_count = 0
		csv_table = csv.reader(archive, delimiter=",")
		next(csv_table, None)  # skip the headers
		i=0
		for row in csv_table:
			#if(i%100==0):
			#		print("Tags = ", i)
			#		end=time.time()
			#		print(end - start)
			#		start=end
			if(i!=0):
				# Insert the tag on the hash table
				entry=hash_tags[maping(row[2].split(" ")[0], NUM_ENTRIES_TAGS)] #entry on the hash table
				j=0
				while(j<len(entry)): #while hasnt reached all elements in the hash entry
					if entry[j][0]==row[2]: #entry[j][0]=tag text
						entry[j].append(row[1]) #Apend the so_fifa id into the tag's list
						break #leave while loop
					j=j+1
				if j==len(entry):
					entry.append([row[2]])#Add a new tag on the list
					entry[j].append(row[1]) #Add the sofifa_id to the tag
			i+=1
	return hash_tags
