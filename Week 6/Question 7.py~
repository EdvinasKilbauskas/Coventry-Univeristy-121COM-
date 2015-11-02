#An anagram of a word is another formed from the same letters. For example, parse and spare are
#anagrams. Create a dictionary where the keys are tuples of letters and the values anagrams they create.
#In Scrabble a player receives a bonus if they play all 7 of their tiles at once, creating an 8 letter word
#(combining with one tile on the board). Which group of 8 letters can create the most words?

""" checks wheter two strings are anagrams """
def areAnagrams(str1, str2):
	#if(len(str1) != len(str2)):
	#	return False
		
	for x in str1:
		hasLetter = False
		for y in str2:
			if(x == y):
				hasLetter = True
		
		if(hasLetter == False):
			return False
			
	return True
	
def getSortedTuple(word):
	l = list(word)
	l.sort()
	t = tuple(l)
	return t

# reads words from the file
f = open("words.txt", 'r')
s = f.read()
words = s.rsplit('\n')
dic = {"":[]}

for word in words:
	t = getSortedTuple(word)
	if(t in dic):
		dic[t].append(word)
	else:
		dic[t] = [word]
	
while(True):
	word = input("Enter word: " )
	print(dic[getSortedTuple(word)])



