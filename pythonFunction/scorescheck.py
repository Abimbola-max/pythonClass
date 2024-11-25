def get_student_scores():
    
	subjects = ["python", "java", "data science", "design-thinking"]
	student_scores = {}

	for names in range(3):
		name = input(f"Enter the name of student {names + 1}: ")
		scores = []
		for subject in subjects:
			score = int(input(f"Enter {name}'s score in {subject}: "))
			scores.append(score)
			student_scores[name] = scores 

	




get_student_scores()