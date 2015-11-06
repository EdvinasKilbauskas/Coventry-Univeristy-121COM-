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

""" read file with words when each word is seperated by a newline ('\n') character """
def readWordsFromFile(filename):
	file = open(filename, 'r')
	data = file.read()
	return data.rsplit('\n')
	
""" creates a dictionary with anagrams """
def createAnagramDictionary(words):
	dic = {"":[]}
	for word in words:
		key = getDictKey(word)
		if(key in dic):
			dic[key].append(word)
		else:
			dic[key] = [word]
	
	return dic
	
""" returns a list of words which you can make using N amount of letters """
def findLongestListOfAnagrams(dic, n):
	length = 0
	longestKey = ()
	for key in dic.keys():
		if(len(key) == n):
			if(len(dic[key]) > length):
				length = len(dic[key])
				longestKey = key
	return dic[longestKey]
	
words = readWordsFromFile("words.txt")
dic = createAnagramDictionary(words)
longestList = findLongestListOfAnagrams(dic,8)

print(longestList)
