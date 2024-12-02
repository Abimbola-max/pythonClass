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



number = int(input("Enter a number between 0 and 1000: "))

while number < 0 or number > 1000:
    print("Invalid input. Please enter a number between 0 and 1000.")
    number = int(input("Enter a number between 0 and 1000: "))

first_digit = number // 100  
second_digit = (number % 100) // 10 
third_digit = number % 10  

sum_of_digits = first_digit + second_digit + third_digit

print(f"The sum of the digits of {number} is: {sum_of_digits}")