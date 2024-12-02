"""

write a program that prompts the user to enter three integers and displays them in increasing order

firstnumber 6
second number 4
third number 7

pseudocode 
1. prompt the user to enter first number
2. collect the number 
3. store as first_number
4. repeat the same process to get second_number and third_number
5. check if the first number is greater than the second number and third 
6. if it is display it first while the rest number follows 
7. repeat the same process for second and third number
8. display result 

"""

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))


if first_number < second_number and first_number < third_number:
  smallest = first_number
elif second_number < first_number and second_number < third_number:
  smallest = second_number
else:
  smallest = third_number


if first_number > second_number and first_number > third_number:
  largest = first_number
elif second_number > first_number and second_number > third_number:
  largest = second_number
else:
  largest = third_number


middle = (first_number + second_number + third_number) - smallest - largest


print(smallest, "," , middle,  ",", largest)


	
		