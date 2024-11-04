/*
convert string to integer


turning strings to text
String text = " "
text + = numberOne;

*/

import java.util.Scanner;

public class StringToInteger {

	public static void main(String... args) {

		Scanner input = new Scanner(System.in);

		System.out.print("Enter a number: ");
		String number = input.nextLine();
		
		
		int convertedNumber = Integer.parseInt(number);

		System.out.print("converted int: " + convertedNumber);
	
}
	}
	