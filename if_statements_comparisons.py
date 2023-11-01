#utilizzeremo gli if ma per comparare dei valori
#ci sono anche valori di comparazione diversi == (uguale a)
#!= (diverso da) < minore <= minore uguale ecc....
def	max_num(num1, num2, num3):
	if num1 >= num2 and num1 >= num3:
		print("The biggest number is " + str(num1))
		return (num1)
	elif num2 >= num1 and num2 >= num3:
		print("The biggest number is " + str(num2))
		return (num2)
	else:
		print("The biggest number is " + str(num3))
		return (num3)

def	equals(num1, num2):
	if num1 == num2:
		print("They are the same number")
	else:
		print("They are not the same number")

def	different(num1, num2):
	if (num1 != num2):
		print("They are not the same number")

print(max_num(390, 40, 5))

#volendo puoi anche comparare le stringhe
