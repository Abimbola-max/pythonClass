import string

encrypt_text = input("Enter your text here: ")
shift_value = 13

def get_encrypted_text(encrypt_text, shift_value):
    for char in encrypt_text:
        if char.isalpha():
            if char.islower():
                original_alphabet_position = ord(char) - ord('a')
                shifted_alphabet_position = (original_alphabet_position + shift_value) % 26
                shifted_text = chr(shifted_alphabet_position + ord('a'))
                result = shifted_text + char













