is_male = True
is_tall = False
#se le condizioni non vengono conseguite
#ciò che riesiede dentro l'if non viene eseguito
#e se inserisci un else statement
#verrà eseguito se l'if è false
if is_male:
	print("You're a male")
else:
	print("You're not a male")
#if statement che controlla entrambi i valori
#is_male e is_tall
if is_male or is_tall: #questo if si verifica quando almeno una delle due variabili è vera
	print("You're male or tall or both")
else:
	print("You're neither tall or male")

#and condition
if is_male and is_tall: #questo if si verifica quando entrambi le variabili sono vere
	print("You're male and tall")
else:
	print("You're not male or not tall")

#anche gli else statement posso eseguire controlli
#nel caso l'if sia falso
#nel caso volessimo controllare altre condizioni extra lo si fa con l'elif (else)
if is_male and is_tall:
	print("You're male and tall")
elif is_male and not(is_tall):
	print("You're a short male")
elif not(is_male) and is_tall:
	print("You're a tall female")
else:
	print("You're not male or not tall")
