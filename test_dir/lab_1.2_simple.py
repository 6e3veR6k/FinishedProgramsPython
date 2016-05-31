


def anti_vowel(text):
	new_string = ''
	for i in text:
		if i not in ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'):
			new_string += i

	print new_string

anti_vowel("Hey look Words!")