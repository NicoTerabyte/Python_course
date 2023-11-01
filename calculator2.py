#1 novembre
#creeremo una calcolatrice avanzata
num1 = float(input("Inserisci il primo numero: ")) #conversione diretta dell'input in float
op = input("Inserisci il tipo di operazione che si vuole eseguire: ")
num2 = float(input("Inserisci il secondo numero: "))

if (op == "+"):
	result = num1 + num2
elif (op == "-"):
	result = num1 - num2
elif (op == "/"):
	result = num1 / num2
elif (op == "*"):
	result = num1 * num2
else :
	print("Damn what did you out")
print(result)
