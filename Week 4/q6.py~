upToTeens = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]

"""asks user input for 4 digit number"""
def getInput():
	while(True):
		number = int(input("Please enter a number between 1 and 9999: "))
		if(number < -9999 or number > 9999):
			print("Error. Try again")
			continue	
		break
	return number
	
"""builds an English sentence for the number given"""
def printSentence(number):
	if(number == 0):
		print("zero", end="")
		return
		
	if(number < 0):
		print('minus', end=" ")
		number *= -1
		
	# extract digits
	d1 = int(number/1000)		# first digit
	d2 = int((number/100)%10)	# second digit
	d34 = int(number%100)		# last 2 digits
	d3 = int((number/10)%10)	# third digit
	d4 = int(number%10)			# fourth digit


	if(d1 != 0):
		print(upToTeens[d1] + ' thousand',end=" ")
	if(d2 != 0):
		print(upToTeens[d2] + ' hundred',end=" ")
		
	if((d1 != 0 or d2 != 0) and (d3 != 0 or d4 != 0)):
		print('and',end=" ")
		
	if(d34 < 20):
		print(upToTeens[d34], end=" ")
	if(d34 >= 20):
		print(tens[d3],end=" ")
		if(d4 != 0):
			print(upToTeens[d4],end=" ")
			
	
"""A function to test the program
   Iterates through a list of pre defined integers, and outputs program results"""
def test():
	test = [0,1,10,15,-20,59,119,500,1018,1030,4000,7005,5010,9999]
	for x in test:
		print(x,end=': ')
		printSentence(x)
		print("") # new line
	

#printSentence(number)
test()