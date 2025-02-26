def get_numbers(numbers):
    output = []
    for number in range(1, numbers):
        print()
    for count in range(1, numbers + 1):
        output.append(count)
    return output
numbers = 5
print(get_numbers(numbers))