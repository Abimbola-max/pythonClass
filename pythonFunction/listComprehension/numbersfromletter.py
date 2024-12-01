def get_letter_out(stringletter):

	return(list(map(lambda x: int(x), filter(lambda x: x.isdigit(),stringletter))))

 