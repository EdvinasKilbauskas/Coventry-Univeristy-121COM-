'''
Download the text file OliverTwist.txt. This is the book Oliver Twist by Charles Dickens as a
text file. The book is out of copyright and so able to be distributed this way. It was obtained from
http://www.textfiles.com/etext/ where many other such books can be found.

The aim of this question is to have Python generate random sentences in English. The basic steps are
below. Hint: start with just the first few lines of the book as a test.
(a) Open the file, read the contents into a string and then close it. Remember that you should use a
try-finally statement to ensure the file closes properly.
(b) Split the string into words.
(c) Create a dictionary whose keys are the words; and values a list of those words that follow the key
word in the text.
(d) Create a random English sentence by: selecting a random word to start with; then adding on one
of the words which follow it in the text; and so on for a set amount of words.
Once you have this working improve the code by:
 Having the process continue until it reaches a word ending with punctuation synonymous with the
end of the sentence (i.e. one of the characters .?!)
 Having the process always start with a word which begins with a capital letter.
Extensions: The output can be improved further by doing the following:
 * Remove the new line characters.
 * Remove the small-print at the start of the book (the first 251 lines)
 * Remove the chapter headings - identified as words all in capitals.
'''

import sys
from random import random
    
""" Replaces multiple characters in a string with a replacement a character """
def replaceChars(string, toRemove, replacement):
	for c in toRemove:
		if(c in string):
			string = string.replace(c,replacement)
	return string
    
""" Reads a file and returns its contents as a string
    Return None if exception is caught """
def readFile(filename, n = -1):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        sys.stderr.write("Error: file couldn't be located")
        return None
    except:
        sys.stderr.write("Error: unknown file error")
        return None
    finally:
        if(n != -1):
            contents = f.read(n)
        else:
            contents = f.read()
            f.close()
    return contents
    
""" Splits a string into a list of words.
    Count is number of words to be returned (use less words for a faster result) """
def getWords(string, count = -1):
    string = replaceChars(string,'\n\r-', ' ')
    string = replaceChars(string, '"()123456789', '')

    tokens = string.rsplit(' ')
    words = list()
    i = 0
    for word in tokens:
        word = replaceChars(word,' ','')
        if(len(word) == 0):
            continue
        if(count != -1 and i == count):
            break

        # remove quotes at the start and end of the word
        if(word[0] == "'"):
            word = word[1:]
        elif(word[len(word)-1] == "'"):
            word = word[:-1]
            
        if(word.isspace() == False):
            words.append(word)
            i += 1
    return words
    
"""  Creates a dictionary whose keys are the words; and values a list of those words that follow the key word in the text. """
def createAWordDictionary(words):
    dic = {str():list()}
    count = len(words)
    for i in range(0,count-1):
        word = words[i]
        following = words[i+1]
        if(word not in dic):
            dic[word] = [following]
        else:
            dic[word].append(following)

    return dic

""" Constructs a random sentence using words given in a dictionary """
def getRandomSentence(dic, startWord):
    word = startWord
    sentence = str()
    while(True):
        sentence = sentence + word + " "
        last = len(word) - 1
        if(last >= 0 and (word[last] == '.' or word[last] == '?' or word[last] == '!')):
            break;
        try:
            followingWords = dic[word]
        except KeyError:
            return None
        if(len(followingWords) != 0):
            word = followingWords[int(random()*(len(followingWords)-1))]	
    return sentence

""" Checks if first and second words of the sentence are uppercase.
    That's enough to know if the sentence is a header """
def isHeader(sentence):
    words = sentence.rsplit(' ')
    if(words[0].isupper() and words[1].isupper()):
        return True
    return False
    
oliverText = readFile("OliverTwist.txt")
words = getWords(oliverText)
print("Total number of words loaded: " + str(len(words)))
dic = createAWordDictionary(words)

while(True):
        word = input("Type a word to begin with: " )
        word = word.capitalize()
        
        sentence = getRandomSentence(dic, word)
        if(sentence == None):
            sys.stderr.write("Error: There's no sentence that starts with '" + word + "'\n")
            continue
        else:
            if(isHeader(sentence)):
                sentence = getRandomSentence(dic, word)
            print(sentence)
