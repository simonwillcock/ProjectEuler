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


if __name__ == '__main__':
	mod = sys.modules[__name__]
	for func in dir(mod):
		callableFunc = getattr(mod, func)
		if callable(callableFunc):
			print(str(func) + ": " + str(callableFunc()))
	
	