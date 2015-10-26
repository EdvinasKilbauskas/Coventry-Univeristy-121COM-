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
	

print(sieveOfEratotosthenes(500))