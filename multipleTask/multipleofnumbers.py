def get_multiple_of_numbers(first_number, second_number, third_number):
    result = []

    for i in range(first_number, second_number + 1):
        if i % third_number == 0:
            result.append(i)

    return result
