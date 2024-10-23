
amount = 1000
annual_rate = 0.07

end_of_year_ten_amount = (amount * (1 + annual_rate) ** 10)
end_of_year_twenty_amount = (amount * (1 + annual_rate) ** 20)
end_of_year_thirty_amount = (amount * (1 + annual_rate) ** 30)

print(f"The amount on deposit at the end of year is: {end_of_year_ten_amount:.2f}, year twenty is: {end_of_year_twenty_amount:.2f} year thirty is: {end_of_year_thirty_amount:.2f}")