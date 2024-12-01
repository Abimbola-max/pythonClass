def multiples_of_3_between_30():
  
  multiples = list() """ or [] """
  for number in range(1, 31):
    if number % 3 == 0:
      multiples.append(number)
  return multiples


result = multiples_of_3_between_30()

print(result) 


def get_multiple_numbers():

	return [x for x in range(3,31,3)]
  
print(get_multiple_numbers())

