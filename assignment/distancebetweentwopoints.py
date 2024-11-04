firstXCoordinate = float(input("Enter the first value of x(x1): "))
firstYCoordinate = float(input("Enter the first value of y(y1): "))
secondXCoordinate = float(input("Enter the second value of x(x2): "))
secondYCoordinate = float(input("Enter the second value of y(y2): "))

if (firstXCoordinate == secondXCoordinate) :
	print("The points are located on a line perpendicular to the x-axis.")
elif (firstYCoordinate  == secondYCoordinate):
	print("The points are located on a line perpendicular to the y-axis.")
else:
	print("The points are not located on a line perpendicular to either axis.")