number = int(input("Enter a five digit number: "))

firstDigit = number // 10000
secondDigit = number // 1000 % 10
thirdDigit = number // 100 % 10
fourthDigit = number // 10 % 10
fifthDigit = number % 10

print(firstDigit, "   " ,secondDigit,"   ",thirdDigit, "   ",fourthDigit "   ",  fifthDigit "   ")