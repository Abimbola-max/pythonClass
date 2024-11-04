<<<<<<< HEAD
letter = str(input("Enter a single character from the alphabet: "))

if len(letter) > 1 or not letter.isalpha():
	print("Error, do the right thing please") 
else: 
	letter = letter.lower()

	if (letter =='a' or letter =='e' or letter =='i' or letter =='o' or letter =='u'):
	   print(letter, " is a vowel");
	else:
=======
letter = str(input("Enter a signle character from the alphabet: "))

if (letter =='a' or letter =='e' or letter =='i' or letter =='o' or letter =='u'):
	   print(letter, " is a vowel");
else:
>>>>>>> e09ac4a5048366362d45aea5187f030e1998b4c2
	   print(letter, " is a consonant");
