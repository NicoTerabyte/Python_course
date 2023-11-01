#il return ci permette effettivamente di avere qualcosa di restituito
#quando gli passiamo un valore per esempio
#piccola nota il return è come una fine per la funzione
#appena la funzione arriva al return tutto ciò che c'è dopo
#verrà ignorato
def cube(num):
	return num*num*num

#result preserverà il valore che viene restituito dalla funzione cube
result = cube(4)
print(result)
