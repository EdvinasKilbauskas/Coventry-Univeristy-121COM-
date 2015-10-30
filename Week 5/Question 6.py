fastPowerCount = 0
powerCount = 0

def fastPower(n,p):
	global fastPowerCount
	fastPowerCount += 1
	if(p == 0):
		return 1
	else:
		if(p % 2 == 1): # p is odd
			return n*fastPower(n*n,(p-1)/2)
		else:			# p is even
			return fastPower(n*n,p/2)

def power(n,p):
	global powerCount
	powerCount += 1
	if(p == 0):
		return 1
	else:
		return n*fastPower(n,p-1)
		

n = 2
p = 10
print("power(" + str(n) + "," + str(p) + ") = " + str(power(n,p)) + " (called " + str(fastPowerCount) + " times)")
print("fastPower(" + str(n) + "," + str(p) + ") = " + str(fastPower(n,p)) + " (called " + str(powerCount) + " times)")