number_of_days = int(input("Enter a number of days: "))

if (number_of_days > 30):
    print("Your membership will be canceled!")

elif (number_of_days > 10):
    print("Your fine is 5 rupees")

elif (number_of_days > 5):
    print("Your fine is one rupee")

elif (number_of_days > 0): 
    print("Your fine is 50 paise")

else:
    print("Invalid input.")