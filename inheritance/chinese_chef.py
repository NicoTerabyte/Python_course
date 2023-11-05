#essendo uno chef specifico questo oltre a fare le cose comuni
#farà delle cose in più
from chef import Chef
#la classe chinese chef eredita da chef tutte le sue funzioni e parametri
#quando questa viene dichiarata all'interno della classe
class Chinese_chef(Chef):
	#possiamo anche sovrascrivere funzioni ereditate
	#cambiandone il risultato
	def make_special_dish(self):
		print("The chef makes orange chicken")
	def make_fried_rice(self):
		print("The chef makes fried rice")
