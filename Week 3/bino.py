def factorial(n): 
	f = 1
	for i in range(2, n+1): 
		f *= i 
	return f 
def series(n,r): 
	rFact = factorial(r) 
	for i in range(0,r+1): 
		riFact = factorial(r-i) 
		iFact = factorial(i) 
		Pow = pow(1,r-i) 
		xPow = pow(r,i) 
		print (int((rFact*Pow*xPow)/(riFact*iFact)),end = " ") 
	




