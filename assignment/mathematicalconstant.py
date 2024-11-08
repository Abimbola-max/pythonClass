import math

for number in range(1,11):
	estimate_e = 1 + 1 / (math.factorial(number))
	
print("The estimated value of e in 10 terms is: ", estimate_e)
	