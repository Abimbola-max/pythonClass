def is_odd(x):
	return x % 2 != 0

numbers = [10,3,7,1,9,4,2,8,5,6]
print(list(filter(is_odd, numbers)))