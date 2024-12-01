import java.util.Scanner;

public class PizzaWahala {

	static Scanner input = new Scanner(System.in);
	static int numberOfGuests;
	static int typeOfPizza;
	static int numberOfSlice;

	public static void main(String[] args) {
		welcomeMessage();
		numberOfGuest();
		typeOfPizza();
		

	}

	public static void welcomeMessage() {
		System.out.println("Welcome to Iya Moses Pizza joint!! The best pizza you would ever get and i can bet that");
	}	

	public static void numberOfGuest() {
		
		System.out.println("Enter number of birthday guests: ");
		numberOfGuests = input.nextInt();

		while (numberOfGuests < 1) {
			System.out.println("You have entered the wrong input. Please enter a number greater than 1 or equals to 1");
			numberOfGuests = input.nextInt();

		}
	}

	public static void typeOfPizza() {

		boolean correctInput = false;

		while (!correctInput) {

		System.out.print("What type of pizza do you want?\n1. Sapa size pizza\n2. small money pizza\n3. big boys pizza\n4. odogwu pizza\n Enter a number >>> ");
		typeOfPizza = input.nextInt();

		switch (typeOfPizza) {
			case 1: 
				int firstTotalSlice = 4;
				int box = 1;
				int remaining = 0;
				int price = 2500;
				int totalPrice = 1;

				if (remaining == 0) {
				box = numberOfGuests / firstTotalSlice;
				remaining = (numberOfGuests % firstTotalSlice);
				totalPrice = box * price;

				}
 
				if (remaining != 0) {
					box = 1 + (numberOfGuests / firstTotalSlice);
					remaining = numberOfGuests % firstTotalSlice;
					totalPrice = box * price;

				}

		System.out.println("You have selected the sapa size pizza\nThe number of boxes you will buy is: " + box + "\nThe remaining of the slices is: " + remaining + "\nThe total amount you are paying is: $" + totalPrice + "\nThank you so much for your patronage!! xx"); correctInput = true; break;

			case 2:
				int secondTotalSlice = 6;
				int secondBox = 1;
				int secondRemaining = 0;
				int secondPrice = 2900;
				int secondTotalPrice = 1;

				if (secondRemaining == 0) {
				secondBox = numberOfGuests / secondTotalSlice;
				secondRemaining = (numberOfGuests % secondTotalSlice);
				secondTotalPrice = secondBox * secondPrice;

				}
 
				if (secondRemaining != 0) {
					secondBox = 1 + (numberOfGuests / secondTotalSlice);
					secondRemaining = numberOfGuests % secondTotalSlice;
					secondTotalPrice = secondBox * secondPrice;

				}

		System.out.println("You have selected the sapa size pizza\nThe number of boxes you will buy is: " + secondBox + "\nThe remaining of the slices is: " + secondRemaining + "\nThe total amount you are paying is: $" + secondTotalPrice + "\nThank you so much for your patronage!! xx"); correctInput = true; break; 
				
			case 3:
				int thirdTotalSlice = 8;
				int thirdBox = 1;
				int thirdRemaining = 0;
				int thirdPrice = 4000;
				int thirdTotalPrice = 1;

				if (thirdRemaining == 0) {
				thirdBox = numberOfGuests / thirdTotalSlice;
				thirdRemaining = (numberOfGuests % thirdTotalSlice);
				thirdTotalPrice = thirdBox * thirdPrice;

				}
 
				if (thirdRemaining != 0) {
					thirdBox = 1 + (numberOfGuests / thirdTotalSlice);
					thirdRemaining = numberOfGuests % thirdTotalSlice;
					thirdTotalPrice = thirdBox * thirdPrice;

				}

		System.out.println("You have selected the sapa size pizza\nThe number of boxes you will buy is: " + thirdBox + "\nThe remaining of the slices is: " + thirdRemaining + "\nThe total amount you are paying is: $" + thirdTotalPrice + "\nThank you so much for your patronage!! xx"); correctInput = true; break;

			case 4:
				int lastTotalSlice = 12;
				int lastBox = 1;
				int lastRemaining = 0;
				int lastPrice = 5200;
				int lastTotalPrice = 1;

				if (lastRemaining == 0) {
				lastBox = numberOfGuests / lastTotalSlice;
				lastRemaining = (numberOfGuests % lastTotalSlice);
				lastTotalPrice = lastBox * lastPrice;

				}
 
				if (lastRemaining != 0) {
					lastBox = 1 + (numberOfGuests / lastTotalSlice);
					lastRemaining = numberOfGuests % lastTotalSlice;
					lastTotalPrice = lastBox * lastPrice;

				}

		System.out.println("You have selected the sapa size pizza\nThe number of boxes you will buy is: " + lastBox + "\nThe remaining of the slices is: " + lastRemaining + "\nThe total amount you are paying is: $" + lastTotalPrice + "\nThank you so much for your patronage!! xx"); correctInput = true; break;


			default:
				System.out.println("You have entered an invalid input");  break;

		}

		}


	}

	
		


	



















}