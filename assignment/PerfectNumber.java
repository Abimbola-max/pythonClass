import java.util.Scanner;

public class PerfectNumber {

	public static void main(String[] args) {

	Scanner input = new Scanner(System.in);

	System.out.print("Enter a number: ");
	int number = input.nextInt();

	int sum = 0;
	int count = 1;

	for (count = 1; count < number; count++) {
		if (number % count == 0) {
			sum += count;
		 }
			}
		if (sum != count) {
		System.out.print("It is not perfect number");
			} else {
		System.out.print("It is a perfect number");
			}	
			
}
   }