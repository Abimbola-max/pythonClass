import math

latitude_of_coordinate1 = float(input("Enter the first latitude of coordinate: "))
longitude_of_coordinate1 = float(input("Enter the second longitude of coordinate: "))
latitude_of_coordinate2 = float(input("Enter the second latitude of coordinate: "))
longitude_of_coordinate2 = float(input("Enter the second longitude of coordinate: "))
radius = 6371.01

distanceBetweenPoints = radius * (math.acos(math.sin(latitude_of_coordinate1))) * math.sin(latitude_of_coordinate2) * math.cos(latitude_of_coordinate1) * math.cos(latitude_of_coordinate2) * math.cos(longitude_of_coordinate1 - longitude_of_coordinate2)

print("The distance between those points is: ", distanceBetweenPoints)