from classes import Test

personality_question = input("What games do you like? FPS, fighting games or platforms ")

lnicoter = Test(personality = "", question = "", answer = "")

if personality_question == "fighting games":
	lnicoter = Test(personality = personality_question, question = "What fighting game do you like in particular? ", answer="guilty gear")
	answer = input(lnicoter.question)
	if answer == lnicoter.answer:
		print("You got me")
else:
	print("Wrong genre think like lnicoter!!!")

