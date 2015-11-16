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
			
	def simplify(self):
		newN = self.n
		newD = self.d
		while(True):
			if(newN % 2 == 0 and newD % 2 == 0):
				newN = newN / 2
				newD = newD / 2
				continue
			if(newN % 3 == 0 and newD % 3 == 0):
				newN = newN / 3
				newD = newD / 3
				continue
			if(newN % 5 == 0 and newD % 5 == 0):
				newN = newN / 5
				newD = newD / 5
				continue
			if(newN % 7 == 0 and newD % 7 == 0):
				newN = newN / 7
				newD = newD / 7
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

