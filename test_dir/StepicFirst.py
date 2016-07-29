def checkio(text):
	VOWELS = "AEIOUY"
	CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

	count = 0

	for i in range(len(text)):
		if (text[i] in VOWELS + VOWELS.lower() and text[i+1] in CONSONANTS + CONSONANTS.lower()) or 
		(text[i] in CONSONANTS + CONSONANTS.lower() and text[i+1] in ) :
			print(el)

checkio("Helo world !")
