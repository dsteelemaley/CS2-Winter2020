#Python3
#------
#Define a function "fibonacci"
def fibonacci(n):
	#initialize the list to store the sequence
	x = [0,1]
	#while loop that ends when the addition is > n
	while x[-1]+x[-2] < n:
		#append the new number to the end of the list
		x.append(x[-1]+x[-2])
	#return the list containing the sequence
	return x

#print the fibonacci sequence under 100
print(fibonacci(100))
