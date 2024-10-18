number = int(input("Enter a number: "))

firstNumber = number % 10
secondNumber = number // 10 % 10
thirdNumber = number // 100

print("The inverse number is: ", firstNumber, secondNumber, thirdNumber)

odd = 0
even = 0
    
if firstNumber % 2 == 0:even += 1
else:odd+=1
    
if secondNumber % 2 == 0:even += 1
else:odd+=1
        
if thirdNumber % 2 == 0:even += 1
else:odd+=1

print("odd number is: " , odd)
print("even number is: " , even)



