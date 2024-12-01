"""
def get_consonant(words: list):
	
	vowel =['a','e','i','o','u']

	return[list(character) for vowel in words if character not in vowel]
"""


def get_consonant(words):
  

  result = []
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  for word in words:
    temp = []
    for char in word:
      if char not in vowels:
        temp.append(char)
    result.append("".join(temp))
  return result


words = ["orange", "Apple", "Ice", "Beans", "Rice"]


no_vowels = get_consonant(words)
print(get_consonant(no_vowels))