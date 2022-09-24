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

