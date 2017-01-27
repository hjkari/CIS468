#!/usr/bin/env python
n = 1
def isPrime(n):
	n = int(input("Enter a number: "))
	if n > 1: #prime numbers are greater than 1
		for i in range (2, n): 
			if (n % i) == 0: #checking if it can be div by 2
				print (n, "is not prime") 
				#prime = False #number is not prime
				break
			else:
				#twin = (n + 2) #prime plus 2 to get twin
				print (n, "is prime.",) 
				#prime = True
				for n in range (1 , n, -2): 
					print (n)
				print("Results: ", n) 
				break

		#return prime

#3def main():

prime = n	
isPrime(n)

#if __name__ == '__main__':
		#main()

#I held out asking for help thinking I'd have an ephiphany to no avail.
#Clearly, I should have caved.

