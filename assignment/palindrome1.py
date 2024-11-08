number = int(input("Enter a three-digit integer: "))

first_digit = number // 100
third_digit = number % 10

if (first_digit == third_digit):
	print(F"{number} is a palindrome")

else:
   	print(f"{number} is not a palindrome")
 