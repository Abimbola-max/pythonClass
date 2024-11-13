def product(*args):   
    product = 1
    for value in args:
        product *= value
    return product


print(product(10, 3, 4))
print(product(1, 15, 3, 4))                    