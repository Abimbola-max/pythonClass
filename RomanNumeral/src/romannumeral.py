def convert_figure_to_roman(number: int):
    if not isinstance(number, int) or number <= 0 or number > 2000:
        raise ValueError("Number must be an integer and must be between 1 and 2000")

    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = []
    for value, numeral in zip(numbers, roman_numerals):
        while number >= value:
            result.append(numeral)
            number -= value
    return ''.join(result)
