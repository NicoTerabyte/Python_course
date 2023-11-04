secret_word = "lnicoter"
guess = ""
guess_count = 0
guess_limit = 3
out_guesses = False

while guess != secret_word and not(out_guesses):
	if guess_count < guess_limit:
		guess = input("Enter guess :")
		guess_count += 1
	else:
		out_guesses = True

if out_guesses:
	print("Sorry bro you got that wrong")
else:
	print("You got it right amazing")
