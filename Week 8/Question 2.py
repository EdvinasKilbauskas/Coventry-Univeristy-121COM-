class Fraction:
	
	def __init__(self,n,d):
		if(type(n) != int):
			raise TypeError("Numerator must be an integer")
		if(type(d) != int):
			raise TypeError("Denominator must be an integer")
		if(d == 0):
			raise RuntimeError("Denominator musn't be zero")
		if(d < 0):
			n = -n
		self.n = n
		self.d = d
		self.simplify()
		
	def __str__(self):
		return str(self.n) + "/" + str(self.d)
		
	def __add__(self, other):
		newN = self.n * other.d + other.n * self.d 
		newD = self.d * other.d
		return Fraction(newN,newD)
		
	def __sub__(self, other):
		newN = self.n * other.d - other.n * self.d 
		newD = self.d * other.d
		return Fraction(newN,newD)
		
	def __mul__(self, other):
		newN = self.n * other.n
		newD = self.d * other.d
		return Fraction(newN,newD)
		
	def __truediv__(self, other):
		newN = self.n * other.d
		newD = self.d * other.n
		return Fraction(newN,newD)
		
	def __eq__(self, other):
		if(self.n * other.d == self.d * other.n):
			return True
		else:
			return False
			
	# used to calculate primes for simplification
	def sieveOfEratotosthenes(n):
		numbers = list(range(2,n))
		primes = list()
		
		while(True):
			if(len(numbers) == 0):
				break
			prime = numbers[0]
			primes.append(prime)
			# remove multiples of the prime
			x = prime
			while(x <= n):
				if(x in numbers):
					numbers.remove(x)
				x += prime
		return primes
			
	def simplify(self):
		primes = Fraction.sieveOfEratotosthenes(max(self.n,self.d))
		newN = self.n
		newD = self.d
		while(True):
			for p in primes:
				if(newN % p == 0 and newD % p == 0):
					newN = newN / p
					newD = newD / p
					continue
			break
		
		self.n = int(newN)
		self.d = int(newD)
		
string = input("Enter two fraction (example: \"1/4 2/5\"): ")
fractions = string.split(' ')
atokens = fractions[0].split('/')
btokens = fractions[1].split('/')

a = Fraction(int(atokens[0]),int(atokens[1]))
b = Fraction(int(btokens[0]),int(btokens[1]))

print(str(a) + " == " + str(b) + " = " + str(a==b))
print(str(a) + " + " + str(b) + " = " + str(a+b))
print(str(a) + " - " + str(b) + " = " + str(a-b))
print(str(a) + " * " + str(b) + " = " + str(a*b))
print(str(a) + " / " + str(b) + " = " + str(a/b))
