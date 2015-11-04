#An anagram of a word is another formed from the same letters. For example, parse and spare are
#anagrams. Create a dictionary where the keys are tuples of letters and the values anagrams they create.
#In Scrabble a player receives a bonus if they play all 7 of their tiles at once, creating an 8 letter word
#(combining with one tile on the board). Which group of 8 letters can create the most words?

""" returns sorted tuple with letters of a word """
def getDictKey(word):
	l = list(word)
	l.sort()
	t = tuple(l)
	return t

""" read file from words when each word is seperated with newline ('\n') char """
def readWordsFromFile(filename):
	file = open(filename, 'r')
	data = file.read()
	return data.rsplit('\n')
	
words = readWordsFromFile("words.txt")

dic = {"":[]}

for word in words:
	t = getDictKey(word)
	if(t in dic):
		dic[t].append(word)
	else:
		dic[t] = [word]
		

length = 0
longestKey = ()
for key in dic.keys():
	if(len(key) == 8):
		if(len(dic[key]) > length):
			length = len(dic[key])
			longestKey = key
	
print(dic[longestKey])


