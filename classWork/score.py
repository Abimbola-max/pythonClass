passed = 0
failed = 0

for count in range(1, 16):
	score = int(input('Enter score: '))
	if(score >= 45):
		passed += 1
		
		
	else:
		failed +=1
		
print('The number of student that passed is ', passed)
print('The number of student that failed is ', failed)	