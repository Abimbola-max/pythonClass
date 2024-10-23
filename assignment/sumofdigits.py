number = int(input("Enter number between 0 - 1000: "))

first_number = number // 100
second_number = (number // 10) % 10
third_number = number % 10

sum_of_digits = first_number + second_number + third_number

print(f"The sum of the digits is {sum_of_digits}")