valid = True

while valid:
    try :
        number_of_students = int(input("Enter the number of students in your class: "))
        number_of_subjects = int(input("Enter the number of subjects offered: "))

        print("Saving >>>>>>>>>>>>>>>>>>>>>>>>")
        print("Saved successfully")
        valid = False
    except ValueError:
        print("Please enter a valid input, enter a number for both number of subject and student.")

def get_details():
    student_data = []

    for count in range(number_of_students):
        continue_loop = True
        while continue_loop:
            try:
                student_name = str(input(f"Enter the name of student {count + 1}: "))
                scores = []

                for counter in range(number_of_subjects):
                    validation = True

                    while (validation):
                        try:
                            score = float(input(f"Enter score for subject {counter + 1} for {student_name}: "))

                            if (score > 0 and score <= 100):
                                print("Saving >>>>>>>>>>>>>>>>>>>>>>>>")
                                print("Saved successfully")
                                scores.append(score)
                                validation = False
                                continue_loop = False

                            else:
                                print("Invalid, Enter score between 1- 100.")

                        except ValueError:
                            print("invalid, Enter numbers only.")

            except NameError:
                print("Please enter a valid input.")

        total = sum(scores)
        average = total / number_of_subjects
        student_data.append([student_name, scores, total, average])

    return student_data

def get_position():
    positions = []
    for count, first_student in enumerate(student_data):
        position = 1
        for counter, other_students in enumerate(student_data):
            if count != counter and other_students[2] > first_student[2]:
                position += 1
        positions.append(position)
    return positions


def print_table():

	print("STUDENT SCORE TABLE")
	print("=========================================================================")

	print("Student", end="\t")
	for counter in range(len(student_data)):
		print(f"sub{counter + 1}", end="\t")

	print("Total\t", "Average\t", "Position\t")	
	print("===========================================================================")

	for count, data in enumerate(student_data):
		name, scores, total, average = data
		print(f"{name}\t", end="")

		for score in scores:
			print(f"{score}\t", end="")
		print(f"{total}\t   {average:.2f}\t     {positions[count]}")

student_data = get_details()
positions = get_position()
print_table()

def subject_summary(student_data, number_of_subjects):
    print("\nSUBJECT SUMMARY")

    for subject_index in range(number_of_subjects):
        failures = 0
        passes = 0

        lowest_student = ""
        lowest_score = 100

        highest_student = ""
        highest_score = 0

        subject_total = 0

        for student in student_data:
            score = student[1][subject_index]
            subject_total += score

            if score > highest_score:
                highest_score = score
                highest_student = student[0]

            if score < lowest_score:
                lowest_score = score
                lowest_student = student[0]

            if score >= 40:
                passes += 1
            else:
                failures += 1

        average_score = subject_total / len(student_data)

        print(f"Subject {subject_index + 1}:")
        print(f"Highest Scoring student is: {highest_student} scoring {highest_score}")
        print(f"Lowest Scoring student is: {lowest_student} scoring {lowest_score}")
        print(f"Overall Total Score for Subject {subject_index + 1}: {subject_total}")
        print(f"Average score for Subject {subject_index + 1} is: {average_score:.2f}")
        print(f"Number of Passes for Subject {subject_index + 1}: {passes}")
        print(f"Number of Fails for Subject {subject_index + 1}: {failures}")

subject_summary(student_data, number_of_subjects)

def class_summary(student_data, number_of_subjects, number_of_students):

    print("\nCLASS SUMMARY")

    highest_total = 0
    highest_student = ""
    lowest_total = 10000
    lowest_student = ""
    class_total_score = 0

    for student in student_data:
        student_total = 0
        for subject_index in range(number_of_subjects):
            student_total += student[1][subject_index]

        class_total_score += student_total

        if student_total > highest_total:
            highest_total = student_total
            highest_student = student[0]

        if student_total < lowest_total:
            lowest_total = student_total
            lowest_student = student[0]

    class_average_score = class_total_score / len(student_data[1])

    print("=================================================================")
    print("\nBest Graduating Student is:", highest_student, "scoring", highest_total)
    print("=================================================================")
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\nWorst Graduating Student is:", lowest_student, "scoring", lowest_total)
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("=================================================================")
    print("\nClass total score is:", class_total_score)
    print(f"Class Average score is: {class_average_score:.2f}")

class_summary(student_data, number_of_subjects, number_of_students)