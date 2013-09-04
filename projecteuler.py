import sys

def Problem1():
	# sum of multiples of 3 and 5 up to 1000
	return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])

def Problem2():
	# Sum of even fibonnaci numbers less than 4,000,000
	
	def genFibsTo(n):
		fibs = [0,1]
		for i in range(2,n+1):
			fibs.append(fibs[-1] + fibs[-2])
		return fibs
	return sum([x for x in genFibsTo(33) if x % 2 == 0])

def Problem3():
	# What is the largest prime factor of the number 600851475143
	def getPrimeFactors(n):
		factors = []
		d = 2
		while n > 1:
			while n % d == 0: # If number is a factor
				factors.append(d)
				n /= d
			d = d + 1

		return factors

	n = 600851475143
	
	return max(getPrimeFactors(n))

def Problem4():
	# Find the largest palindrome made from the product of two 3-digit numbers.
	
	def isPalindrome(n):
		num_string = str(n)
		return num_string == num_string[::-1]

	
	palindromes = []
	i = 999
	while i > 1:
		for n in range(100,1000)[::-1]:
			palindrome = isPalindrome(n * i)
			if palindrome == True:
				palindromes.append(n * i) 
				break
		i -= 1
	return max(palindromes)

def Problem5():
	# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

	return max([x for x in range(20,1000000000) if 
		x % 1 == 0 and 
		x % 2 == 0 and 
		x % 3 == 0 and 
		x % 4 == 0 and 
		x % 5 == 0 and 
		x % 6 == 0 and 
		x % 7 == 0 and 
		x % 8 == 0 and 
		x % 9 == 0 and 
		x % 10 == 0 and 
		x % 11 == 0 and 
		x % 12 == 0 and 
		x % 13 == 0 and 
		x % 14 == 0 and 
		x % 15 == 0 and 
		x % 16 == 0 and 
		x % 17 == 0 and 
		x % 18 == 0 and 
		x % 19 == 0 and 
		x % 20 == 0 
		])
	

def Problem6():
	# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
	sum_of_squares = 0
	square_of_sums = 0
	for i in range(101):
		square_of_sums += i

	# Yay list comprehensions!
	sum_of_squares = sum([x**2 for x in range(101)])
	
	return (square_of_sums**2) - sum_of_squares

def Problem7():
	# What is the 10 001st prime number?
	def isPrime(i):
		if i <= 1:
			return False
		elif i == 2:
			return True
		elif i % 2 == 0:
			return False

		counter = 3
		while (counter * counter) <= i:
			if i % counter == 0:
				return False
			else:
				counter += 2
		return True

	numPrimes = 1
	curNum = 1
	while numPrimes < 10001:
		curNum = curNum + 2
		if isPrime(curNum):
			numPrimes += 1
	return curNum

if __name__ == '__main__':
	print(Problem7())
	
	