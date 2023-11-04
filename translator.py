#The giraffe language
#vowels -> g, dog = dgg, cat = cgt
#faremo un traduttore per cambiare le vocali con la g
def	translate(phrase):
	translation = ""
	for letter in phrase:
		if letter.lower() in "aeiou": #in python puoi controllare un caratter in un range preciso
			if letter.isupper():
				translation += "G"
			else:
				translation += "g" #la stringa è vuota se la lettera è una vocale inseriamo g
		else:
			translation += letter
	return (translation)

print(translate(input("Enter the word to translate: ")))
