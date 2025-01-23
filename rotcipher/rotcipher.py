def get_encrypted_text(words, shift_value):
    encrypted_text = ""
    for char in words:
        if char.islower():
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            index = alphabet.index(char)
            shifted_index = (index + shift_value) % 26
            shifted_char = alphabet[shifted_index]
            encrypted_text += shifted_char
        elif char.isupper():
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            index = alphabet.index(char)
            shifted_index = (index + shift_value) % 26
            shifted_char = alphabet[shifted_index]
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text
















