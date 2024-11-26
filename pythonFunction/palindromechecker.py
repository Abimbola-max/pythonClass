def is_palindrome(number):

	originalNumber = number;
 
	reversedNumber = 0;

	while (number != 0):

		lastDigit = number % 10

		reversedNumber = reversedNumber * 10 + lastDigit

		number /= 10 
        	
	return originalNumber == reversedNumber


