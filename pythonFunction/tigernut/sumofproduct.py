def get_sum_of_product(number):

    sum = 0

    for count in range(len(number)):
        for counts in number:
            sum += counts
        sum -= number[count] 
    return sum



