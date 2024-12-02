def cube(number):
	cube = []
	for count in range(1, 6):
		cube.append(count**3)
	return cube



def get_cube(number):
	return(cube([i for i in range(1,6)]))

print(get_cube(6))