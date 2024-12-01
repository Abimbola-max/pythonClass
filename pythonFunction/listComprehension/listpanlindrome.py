def get_palindrome(text: list):

    result = []

    for word in text:
        count = 0
        counter = -1
        is_palindrome = True 

        while count <= len(word) // 2:
            if word[count] != word[counter]:
                is_palindrome = False
                break
            count += 1
            counter -= 1

        result.append(is_palindrome)

    return result

text = ['madam', 'apple', 'racecar']
print(get_palindrome(text))