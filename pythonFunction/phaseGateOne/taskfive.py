"""
write a program that prompts the user to enter an integer for todays day of the week(Sunday is 0,  Monday is 1 and Saturday is 6) also prompt the user to enter the numbers of days after today for a future day and display the future day of the week.

enter today's day
enter the number of days elapsed since today 
today is Monday and the future day is Thursday

pseudocode 
prompt the user to enter an integer 
collect it
store as number
prompt the user to enter number of days after today
collect it
store as numberOfDays
if user enter 0, display sunday
if the user enter 2, for the future day, display Tuesday
repeat the same process to cover the whole number of days
display result

"""

#import date

def get_inputs():

	number = int(input("Enter today's day: "))

	number_of_days = int(input("Enter the number of days elapsed since today: "))

	#start_date = date.date

	"sunday" == "0"
	"monday" == "1"
	"tuesday" == "2"
	"wednesday" == "3"
	"thursday" == "4"
	"friday" == "5"
	"saturday" == "6"

	if number == 0:	
		print("Today is Sunday")
	elif number == 1:	
		print("Today is Monday")
	if number == 2:	
		print("Today is Tuesday")
	if number == 3:	
		print("Today is Wednesday")
	if number == 4:	
		print("Today is Thursday")
	if number == 5:	
		print("Today is Friday")
	if number == 6:	
		print("Today is Saturday")

number = get_inputs()

def get_future_date():
	

	if number == 0:	
		print("Today is Sunday")
	elif number == 1:	
		print("Today is Monday")
	if number == 2:	
		print("Today is Tuesday")
	if number == 3:	
		print("Today is Wednesday")
	if number == 4:	
		print("Today is Thursday")
	if number == 5:	
		print("Today is Friday")
	if number == 6:	
		print("Today is Saturday")

	
get_future_date()
	








