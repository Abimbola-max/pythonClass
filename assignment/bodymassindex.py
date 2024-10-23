weight_in_pounds = float(input("Enter weight in pounds: "))
height_in_inches = float(input("Enter height in inches: "))

body_mass_index = (weight_in_pounds / (height_in_inches * height_in_inches))

print(f"The body mass index is {body_mass_index:.2f}")
