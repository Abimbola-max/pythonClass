def only_floats(a,b):
	if a < 0 and b > 0:
		return 4

	elif a > 0 and b < 0:
		return 3

	if type(a) is float and type(b) is  float:
        	return 2
    
	elif type(a) is float or type(b) is  float:
		
        	return 1

	else:
        	return 0

	



