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