# coding=utf-8
# In the separate Python file MusicAPIFunctions.py I have defined 2 functions.
# The next line allows those functions to be used in this script.

from MusicAPIFunctions import checkSpotifyPopularity, printRadioOnePlaylist

# The functions use information stored on the internet regarding music.
# We give examples of each

print("-"*50)
print("Usage:")
print("type \"playlist [letter]\" following a playlist letter (A,B,C or I) to print a playlist")
print("type \"compare [artist1]:[artist2]\" to compare artists by popularity")
print("type \"quit\" to quit")
print("-"*50)

while(True):
	cmdStr = input("cmd:/ ")
	tokens = cmdStr.split(' ',1)
	
	if(len(tokens) < 2):
		print("Invalid command. Try again")
		continue
	
	cmd = tokens[0].upper()
	
	if(cmd == "PLAYLIST"):
		if(len(tokens) < 2):
			print("Invalid format. Try again")
			continue
		
		letter = tokens[1].upper()
		printRadioOnePlaylist(letter)
		
	elif(cmd == "COMPARE"):
		artists = tokens[1].split(":")
		
		if(len(tokens) < 2):
			print("Invalid format. Try again")
			continue
		
		artist1 = artists[0]
		artist2 = artists[1]
		rank1 = int(checkSpotifyPopularity(artist1))
		rank2 = int(checkSpotifyPopularity(artist2))
		
		print("-"*50)
		if(rank1 < rank2):
			print(artist1.upper() + "(rank: " + str(rank1) + ") is more popular than " + artist2.upper() + "(rank: " + str(rank2) + ")")
		elif(rank2 < rank1):
			print(artist2.upper() + "(rank: " + str(rank2) + ") is more popular than " + artist1.upper()	+ "(rank: " + str(rank1) + ")")
		else:
			print("You can't compare artist to himself. Try again.")
			continue
		print("-"*50)
	
	elif(cmd == "QUIT"):
		break
	
#checkSpotifyPopularity(artist)
#printRadioOnePlaylist(Letter)
#


