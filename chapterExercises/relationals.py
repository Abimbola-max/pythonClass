print('Enter two integers and i will tell you the relationships they satisfy')

NUMBER_ONE = int(input('Enter first number: ')) 
NUMBER_TWO = int(input('Enter second number: ')) 

if (NUMBER_ONE > NUMBER_TWO):
	print(NUMBER_ONE, 'is greater', NUMBER_TWO)
	if (NUMBER_ONE >= NUMBER_TWO):
		print(NUMBER_ONE , 'is greater than or equals to', NUMBER_TWO)
	if (NUMBER_ONE != NUMBER_TWO ):
		print(NUMBER_ONE , 'is not equals to', NUMBER_TWO)


elif (NUMBER_ONE < NUMBER_TWO ):
	print(NUMBER_ONE, 'is less', NUMBER_TWO)
	if (NUMBER_ONE <= NUMBER_TWO ):
		print(NUMBER_ONE , 'is less than or equals to', NUMBER_TWO)
	if  (NUMBER_ONE != NUMBER_TWO ): 
		print(NUMBER_ONE , 'is not equals to', NUMBER_TWO)
else:
	print(NUMBER_ONE , 'is equals to', NUMBER_TWO)




