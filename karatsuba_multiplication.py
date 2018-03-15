'''
Karatsuba algorithm for integer multiplication

input: x1, x2

algorithm:
Let x1 = a*10^(n/2)+b and x2 = c*10^(n/2)+d, where n is the length of x1 and x2.
multiply(x1, x2):
	recursively compute a*c --(1)
	recursively compute b*d --(2)
	recursively compute (a+b)*(c+d)  --(3)
	compute (4) = (3)-(2)-(1)
	return (1)*10^n + (2) + (4)*10^(n/2)
'''
import numpy as np
import sys

# Get the two integers to multiply
try:
	input1 = int(sys.argv[1])
	input2 = int(sys.argv[2])
except IndexError:
	print("input values were not given")
	sys.exit()

def multiply(x1, x2):
	# Get the length of input x1 and x2
	x1size = len(str(x1))
	x2size = len(str(x2))
	
	if (x1size==1 or x2size==1):
		return x1*x2
	else:	
		half_size = max(x1size, x2size)//2
		
		# x1 = a*10^(n/2)+b
		# x2 = c*10^(n/2)+d
		a = x1 // 10**half_size
		c = x2 // 10**half_size
		b = x1 % 10**half_size
		d = x2 % 10**half_size
		
		# Step 1. Recursively compute ac
		ac = multiply(a,c)
		
		# Step 2. Recursively compute bd
		bd = multiply(b,d)
		
		# Step 3. (a+b)*(c+d)
		prod3 = multiply(a+b, c+d)
		
		# Step 4. (3) - (2) - (1)
		prod4 = prod3 - bd - ac
		
		# Step 5. final product value
		return (ac * 10**(2*half_size) + bd + prod4 * 10**half_size)
		
if __name__=='__main__':
	result = multiply(input1, input2)
	print(result)