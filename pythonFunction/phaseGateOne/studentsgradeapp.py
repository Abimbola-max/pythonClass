def for_all_input():
    number_of_students = int(input("Enter the number of students in your class: "))

    student_scores = []

    for count in range(number_of_students):
        no_of_all_subjects = int(input(f"Enter number of subjects for student {count + 1}: "))

        scores = []

      
        for count in range(no_of_all_subjects):
            score = float(input(f"Enter scores for student {count + 1}: "))
            scores.append(score)

        student_scores.append(scores)
        total = sum(scores)  
        average = total / no_of_all_subjects

        print(f"The total grade for student {count + 1} is: {total}")
        print(f"The average grade for student {count + 1} is: {average}")

for_all_input()

def print_table(no_of_all_subjects, score, total, average):

	#first_function = for_all_input()
	print("STUDENT SCORE TABLE")
	print("-----------------------------------------------------")
	print("subject", "score", "Total", "Average", "position")
	
	
	for subject in no_of_all_subjects:
		print(subject, "\t", score[subject], "\t", total[subject], "\t", average[subject], "\t", "-") 

	print("-----------------------------------------------------")




	

print_table(number_of_students, no_of_all_subjects, score, total, average)
































































