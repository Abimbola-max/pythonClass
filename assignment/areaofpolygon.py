import math

sideOnThePolygon = int(input("Enter the number of sides on the polygon: "))
length = int(input("Enter the length of one of the sides: "))

areaOfAPolygon = float(sideOnThePolygon * length ** 2) / (4 * math.tan((3.142) / sideOnThePolygon))

print("The area is : " , areaOfAPolygon)

