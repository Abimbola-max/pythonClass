def number_occurrence(numbers):

	output = {}
	zeroOccurrence = 0;
	oneOccurrence = 0;
	twoOccurrence = 0;
	threeOccurrence = 0;
	fourOccurrence= 0;
	fiveOccurrence = 0;
	sixOccurrence = 0;
	sevenOccurrence = 0;
	eightOccurrence = 0;
	nineOccurrence = 0;
	

	for count in numbers:
		if count == 0:
			zeroOccurrence += 1
			output.append(zeroOccurrence)
		elif count == 1:
			oneOccurrence += 1
			output.append(oneOccurrence)
		elif count == 2:
			twoOccurrence += 1
			output.append(twoOccurrence)

		elif count == 3:
			threeOccurrence += 1
			output.append(threeOccurrence)

		elif count == 4:
			fourOccurrence += 1
			output.append(fourOccurrence)

		elif count == 5:
			fiveOccurrence += 1
			output.append(fiveOccurrence)

		elif count == 6:
			sixOccurrence += 1
			output.append(sixOccurrence)

		elif count == 7:
			sevenOccurrence += 1
			output.append(sevenOccurrence)

		elif count == 8:
			eightOccurrence += 1
			output.append(eightOccurrence)

		else:
			nineOccurrence += 1
			output.append(nineOccurrence)
