def get_multiple_of_numbers(first_one, second_num, third_number):
    result = []
    while third_number < second_number:
        answer = third_number * third_number
        result.append(answer)

    return result

first_one = 1
second_num = 10
third_number = 2

print(get_multiple_of_numbers(first_one, second_num, third_number))
