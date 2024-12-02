def  get_details():
	fullName = input("Enter your name: ")
        age = input("How old are you?")

	if (age < 10 or age > 65):
		print("Sorry, This App Is Not Suitable For Your Age.")
            	Sys.exit()
		print()
    	
def get_last_period_info():
	lastPeriodDay = input("Enter the first date of your last period: ");
        
	while (lastPeriodDay < 1 or lastPeriodDay > 31):
		lastPeriodDay = input("Invalid day input. Please enter a day between 1 and 31: ")
		
		lastPeriodMonth = input("Enter your last period month: ")

		while (lastPeriodMonth < 1 or lastPeriodMonth > 12):
			lastPeriodMonth = input("Invalid day input. Please enter a month between 1 and 12: ")

		currentYear = input("Enter year: ")

		periodDuration = input("How long does your period last for?")

		if (periodDuration < 1 or periodDuration > 8):
			print("Enter a valid input!!")
		
def display_welcoming_code():
	print("Welcome To Bibi's MenstrualCycle App!");
        	
def display_welcome():
	print(f"Welcome ", {fullName})
  
def  get_gender():

	gender = input("Kindly Enter Your Gender (male/female): ")

	if (gender.equals("F") or gender.equals("M")) 
			
	if (gender.equals("F")):
		print("Hi sis!!")

	elif (gender.equals("M")):
		print("You are at the right place for your babe or hmm.")
     
	else:
		print("Invalid Input. Please Enter 'M' for Male or 'F' for Female.")
            
	return gender
	
def  moodOf():
	periodMood = input("How do you feel about your period?" + "\n 1. It is a love hate relationship" + "(:(" + "\n2. Embarassed" + ":( " + "\n3. Hate it" + "\n4. We've become friends" + ":)" + "\n>>>")

		match (periodMood):
			case 1: 
				print("I get it lol. You are relieved when you see it but can not wait to let it go")
			case 2: 
				print("It is normal to feel a bit uncomfortable talking about periods")
			case 3: 
				print("You are not alone, many people feel the same way about their periods")
			case 4: 
				print("We love to hear it!! WE will hep  you live in harmony with your period by predicting correctly ")

			case _:
				print("Enter the correct input my guy");

def calculate_estimates():
        
	nextPeriodDay = lastPeriodDay
	duration = nextPeriodDay + 5
	nextPeriodMonth = lastPeriodMonth + 1
	if (nextPeriodMonth > 12):
		nextPeriodMonth = 1
		currentYear+=1

        
	ovulationDay = nextPeriodDay - 14
	ovulationMonth = nextPeriodMonth
	ovulationYear = currentYear
	if (ovulationDay <= 0): 
		ovulationMonth--
		if (ovulationMonth == 0):
			ovulationMonth = 12 
			ovulationYear-=1;

	ovulationDay += numberOfDaysInMonth(ovulationYear, ovulationMonth); 
       

	safePeriodStartDay = ovulationDay - 7
	safePeriodStartMonth = ovulationMonth
	safePeriodStartYear = ovulationYear
	if (safePeriodStartDay <= 0): 
		safePeriodStartMonth--;
		if (safePeriodStartMonth == 0):
			safePeriodStartMonth = 12
			safePeriodStartYear-=1 

	safePeriodStartDay += numberOfDaysInMonth(safePeriodStartYear, safePeriodStartMonth)
        

	safePeriodEndDay = ovulationDay + 7;
	safePeriodEndMonth = ovulationMonth;
	safePeriodEndYear = ovulationYear;

	if (safePeriodEndDay > numberOfDaysInMonth(safePeriodEndYear, safePeriodEndMonth)):
		safePeriodEndDay -= numberOfDaysInMonth(safePeriodEndYear, safePeriodEndMonth);
		safePeriodEndMonth++
		if (safePeriodEndMonth > 12):
                safePeriodEndMonth = 1
                safePeriodEndYear+=1
                
print(f"\nYour next period date should be: ", {nextPeriodDay}, "/", 
                           {nextPeriodMonth} , "/" , {currentYear}, "to", {duration}, "/" + 
                           {nextPeriodMonth}, "/",  {currentYear})
print(f"Your estimated ovulation date: " , {ovulationDay} , "/" , 
                           {ovulationMonth} + "/" , {ovulationYear});
        System.out.println("Your estimated safe period is: " , 
                           {safePeriodStartDay}, "/", {safePeriodStartMonth}, "/" ,{safePeriodStartYear}, " to ",
                           {safePeriodEndDay} , "/" , {safePeriodEndMonth} , "/" , {safePeriodEndYear})
   

def number_of_days_in_month(int year, int month):
        
	if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or 
            month == 10 or month == 12):

		return 31

	elif (month == 4 or month == 6 or month == 9 or month == 11):
		return 30

	else:
		return 28
 
 