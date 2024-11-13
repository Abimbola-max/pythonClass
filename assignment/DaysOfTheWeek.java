import java.util.Scanner;

public class DaysOfTheWeek {

	public static void main(String... args) {

		Scanner input = new Scanner(System.in);

		System.out.print("Enter a number within 1-7: ");
		int reply = input.nextInt();

		switch (reply) {
		case 1:
			System.out.print("Monday"); break;

		case 2:
			System.out.print("Tuesday"); break;

		case 3:
			System.out.print("Wednesday"); break;
		
		case 4:
			System.out.print("Thursday"); break;

		case 5:
			System.out.print("Friday"); break;

		case 6:
			System.out.print("Saturday"); break;

		case 7:
			System.out.print("Sunday"); break;

		case _:
			System.out.print("input the right number, arghhh!"); break;

	}
    }
}











