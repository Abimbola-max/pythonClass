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


no_vowels = remove_vowels(words)
print(def get_consonant(no_vowels))