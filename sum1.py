number = (input("Enter a number: "))

firstNumber = int(number / 100)
secondNumber = int(number // 10) % 10
thirdNumber = (number % 10)

sum = int(firstNumber + secondNumber + thirdNumber)
print(sum)
	