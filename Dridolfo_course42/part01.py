#Classi in python
#in python accedi con il punto ai valori della classe
# __init__ è un metodo
# dunder methods metodi che sono scritti in questa maniera:
# __method__ e servono a interefacciare la classe
#__init__ è molto famoso e praticamente sarebbe il costruttore della classe python
#__dir__ ritorna tutti i metodi dell'oggetto

class Ciao:
	def __init__(self):
		pass

class Test:
	def __init__(self):
		print("Constructor invoked")
		#definiamo gli attributi
		#Gli attributi è sempre meglio dichiararli nel costruttore anche se
		#è possibile dichararli in seguito
		self.name = "Lorenzo"
		self.age = 21
		self.greet = Ciao()

	#si trigghera quando l'oggetto viene castato in una sstringa
	def __str__(self):
		return "Questo è un oggetto Test"

	#metodi statici, quando non uso la variabile self
	#le cose che hanno @ si chiamano "decorators" cioè delle funzioni eseguite prima della dichiarazione
	#della funzione, e NON può accedere agli attributi della classe
	@staticmethod
	def save():
		return "Daje"


#dimostriamo che i valori della classe possono essere toccati da fuori
class Studente:
	def __init__(self, nome, cognome, nome_intra):
		print("Studente constructor called")
		self.nome, self.cognome, self.nome_intra = nome, cognome, nome_intra

		#questa variabile non comparirà quando vuoi modificarla
		self._noTouch = "variabile che secondo pep8 non dovresti modificare"

	def __str__(self):
		return self.nome + " " + self.cognome + " " + self.nome_intra

	@staticmethod
	def studio():
		print("pausa caffè")


#Questa classe erediterà da studente
class QuarantaDueRoma(Studente):

	#Inizializzazione di una super classe
	#abbiamo usato **kwargs che è un dizionario che prende dal costruttore stesso

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

#con questa definizione la funzione lavora anche senza parametri se no con solo
#"topolino" darebbe errore
def pippo(ciao="", topolino=None):
		print(ciao, topolino)

# t = Test()
# print(str(t), t)

def main():
	lorenzo = Studente(nome="lorenzo", cognome="nicotera", nome_intra="lnicoter")

	# print(lorenzo)
	# lorenzo.nome = "Venelin"
	# print(lorenzo)
	li = ["ciao", "topolino"]
	#il * è per splittare la lista
	# test = QuarantaDueRoma(lorenzo)
	# print(test)
	pippo(*li)
	pass

main()
