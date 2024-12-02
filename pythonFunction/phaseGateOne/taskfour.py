"""

1. generates random subtraction problems 
ensure the first is greater than the second one 
2. presents problem in correct order
	display each problems sequently 
3. allow user take up to 10 questions
give user 1 attempt per problem 
4. calculates and display a final score
determine the score based on the number of correct answers
measures and displays time taken 
record the start and end times to calculate the total time in seconds


pseudocode 
1. generate first number 
2. store as first_number
3. generate second question to be from 1 to the range of first number
4. store as second_number
5. return both numbers(first_number and second_number)
6. to get the score and time taken:
	initialized the variable score to be zero
	initialized the variable answer to be the subtraction of both numbers
7. the questions should be generated 10 times
8. if answer is equals to the subtraction of both first_number and second_number
9. add 1 to score 
10. if it is not, display an error message
11. to get the total score subtract the total number of correct answer by 10
12. to get the time taken: minus the time the program started running from the end time
13. display total
14. display the total time taken
 
"""
import random
import time

def generate_questions():
    

    first_number = random.randrange(1, 101) 
    second_number = random.randrange(1, first_number)
  
    return first_number, second_number

def get_score_and_time_taken():
    

    score = 0
    start_time = time.time()  

    for count in range(1, 11):  
        number_one, number_two = generate_questions()
        answer = int(input(f"What is {number_one} - {number_two}? "))
        if answer == number_one - number_two:
            print("You got it!")
            score += 1
        else:
            print(f"Incorrect. The answer is {number_one - number_two}")

    end_time = time.time()  
    time_taken = end_time - start_time

    print(f"\nYour final score: {score}/10")
    print(f"The time taken: {time_taken:.2f} seconds") 

get_score_and_time_taken()