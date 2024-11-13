answer = int(input("Choose a Shape you want to calculate the area for:\n1. Circle\n2. Rectangle\n3. Triangle\n>>>"))
	
match (answer):

	case 1: 
		radius = float(input("Enter the radius: "))
		circleArea = float(3.1459 * radius * radius)
		print(f"The area of the circle is {circleArea:.2f}")
			
	case 2: 
		length = float(input("Enter the length: "))
		width = float(input("Enter the Width: "))
		rectangleArea = length * width
		print(f"The area of the Rectangle is {rectangleArea:.2f}")
			
	
	case 3: 
		base = float(input("Enter the base of the triangle: "))	
		height = float(input("Enter the Height: "))
		triangleArea = 0.5 * base * height
		print(f"The area of the Triangle is {triangleArea:.2f}")

	case _:
		print("Enter valid input")
