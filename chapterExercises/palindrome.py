number = int(input("Enter a five digit number: "))

firstDigit = number // 10000
lastDigit = number % 10

if firstDigit == lastDigit:
	print(number, 'is a palindrome')

else:
	print(number, 'is not a palindrome')

