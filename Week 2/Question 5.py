hours = -1
minutes = -1
timeStr = ""

numbers = ["zero", "one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]

while(True):
	strng = input("Enter time (example 15:43): ")
	
	tokens = strng.split(":")
	
	if(len(tokens) < 2 ):
		print("Invalid format. Try again")
		continue
	
	hours = int(tokens[0])
	minutes = int(tokens[1])
	
	if(minutes < 0 or minutes > 60 or hours < 0 or hours > 23 ):
		print("Invalid format. Try again")
		continue
		
	break
	
	
if(hours > 12):
	daytime =  "afternoon"
	hours -= 12
else:
	daytime = "morning"
	
	
minuteStr = ""
if(minutes > 15 and minutes < 45):
	minuteStr = "half past "
if(minutes >= 45):
	hours += 1
	

sentence = "The time is about " + minuteStr + numbers[hours] + " in the " + daytime

print(sentence)