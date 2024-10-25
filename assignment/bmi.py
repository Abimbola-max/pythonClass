weight_in_kilogram = float(input("Enter weight in kilogram: "))
height_in_meters = float(input("Enter height in meters: "))

weight_in_pounds = weight_in_kilogram * 0.45359237
height_in_inches = height_in_meters * 0.0254

body_mass_index = weight_in_pounds / (height_in_inches * height_in_inches)

print(f"Body mass index is: {body_mass_index:.4f}")
