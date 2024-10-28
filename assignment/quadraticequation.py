import math

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
c = int(input("Enter the third value; "))

determinant = float (b*b - 4*a*c)
print("The determinant is: ", determinant)

if determinant > 0:
 result1 = (-b + (math.sqrt(determinant))) / 2 * a
 result2 = (-b - (math.sqrt(determinant))) / 2 * a

 print('The first result is: ', result1)
 print('The second result is: ', result2)

elif determinant == 0:
  result3 = -b / (2 * a)
  print("The result is: ", result3)

else:
  print("NaN")


