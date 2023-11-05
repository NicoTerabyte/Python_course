#con le classi definisci i tuoi dati unici
#nella classe studente abbiamo una funzione per
#inizializzare i suoi attributi
#con self stiamo specificando chi stiamo inizializzando
#cioè la classe, subito dopo definiamo i parametri che stanno nella classe
#e che devono essere inizializzati
'''
perché ha fatto questo nell'inizializzazione?
		self.name = name
		self.major = major
		self.gpa = gpa
		self.is_on_probation = is_on_probation
Quello che succede è che quando creiamo un oggetto con la classe studente
i valori inseriti vengono mandati alla funzione __init__
i quali sono diversi dai valori self.name ecc... perché venogno definiti
appunto con i valori passati quando creiamo un oggetto
per esempio il nome dello studente saràa uguale al nome che abbiamo passato
'''
class Student:

	def	__init__(self, name, major, gpa, is_on_probation):
		self.name = name
		self.major = major
		self.gpa = gpa
		self.is_on_probation = is_on_probation
