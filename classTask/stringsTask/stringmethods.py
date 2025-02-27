from collections import Counter

def get_count(input_string: str):
    result = {}
    for char in input_string:
        counter = 0
        for char2 in input_string:
            if char == char2:
                counter += 1
                result[char] = counter
    return result


def swap_string_and_strip(first_input_string: str, second_input_string: str) -> str:
    first_swap = second_input_string[:2] + first_input_string[2:]
    second_swap = first_input_string[:2] + second_input_string[2:]
    return first_swap + " " + second_swap


def divide_and_insert(input_string: str, second_input: str) -> str:
    if len(input_string) % 2 == 0:
        return input_string[:len(input_string) // 2] + second_input + input_string[len(input_string) // 2:]
    else:
        return input_string + '' + second_input


def display_upper_case_first(input_string: str) -> str:
    upper_case = ''
    lower_case = ''
    for char in input_string:
        if char.isupper():
            upper_case += char
        else:
            lower_case += char
    return upper_case+lower_case

def get_number_of_char(input_string: str, input_char) -> tuple[str, int]:
    count = 0
    for char in input_string:
        if input_char == char:
            count += 1

    return input_char, count

def remove_character(input_string: str) -> str:
    upper_container = ''
    for char in input_string:
        if char.isalpha():
            upper_container += char
    return upper_container

# def swap_string_and_strip_two(input_string: str):


