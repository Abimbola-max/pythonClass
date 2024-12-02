"""
write a program that reads an integer between 0 and 1000 and adds all the digits in the integer. 

for example , if an integer is 932, the sum of all its digit is 14

pseudocode
prompt the user to enter a number from 1 - 100
collect the number 
store as number
to get the first number, divide first number by 100
store as firstNumber
repeat the same process to get secondNumber and thirdNumber
to get the sum:
add firstNumber, secondNumber and thirdNumber together
store as sum
display sum

"""



number = int(input("Enter a number: "))

if number < 1 or number > 1000:
	print("Enter a correct value")

firstNumber = int(number // 100)
secondNumber = int(number // 10) % 10
thirdNumber = (number % 10)

sum = int(firstNumber + secondNumber + thirdNumber)
print(f"The sum of the number input is: {sum}")
