#in questa lezione gestiamo il codice quando succedono degli errori
#mettendo la situzione in un try in caso di errore mandiamo l'except
#così il programma non si romperà nel caso non venga inserito il valore correttamente
#possiamo anche specificare quale errore andiamo a gestire
#esistono vari tipi di exception a quanto pare
#perché ZeroDivisionError e ValueError sono due flag tipo
#si può anche chiedere al debugger di dirci cosa è andato storto con as
#una good practice è di essere specifici con gli errori
try:
	value = 10/0
	number = int(input("Inserisci un numer: "))
	print(number)
except ZeroDivisionError as err:
	print(err)
except ValueError:
	print("Invalid input")
