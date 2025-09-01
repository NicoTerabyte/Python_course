# metodo 1 che controlla chi vince tra le due in velocità massima
# metodo 2 che controlla se le due macchine hanno la stessa vernice
class Auto:
	def __init__(self, vernice, prezzo, posti, anno):
		self.vernice, self.prezzo, self.posti, self.anno = vernice, prezzo, posti, anno

	def sameVernice(self, other):
		if self.vernice == other:
			return True
		else:
			return False

	def __str__(self):
		return self.vernice, self.prezzo, self.posti, self.anno


class Ferrari(Auto):
	def __init__(self, *args, modello, velocita_massima, cavalli):
		super().__init__(*args)
		self.modello, self.velocita_massima, self.cavalli = modello, velocita_massima, cavalli

	def fastest(self, rival):
		if max(self.velocita_massima, rival) == self.velocita_massima:
			print("la più veloce è la ferrari!!")
			return True
		else:
			print("il rivale è più veloce")
			return False

	def __str__(self):
		return self.modello

class Mercedes(Auto):
	def __init__(self, *args, modello, velocita_massima, cavalli):
		super().__init__(*args)
		self.modello, self.velocita_massima, self.cavalli = modello, velocita_massima, cavalli

	def fastest(self, rival):
		if max(self.velocita_massima, rival) == self.velocita_massima:
			print("la più veloce è la Mercedes!!")
		else:
			print("il rivale è più veloce")


class Redbull(Auto):
	def __init__(self, *args, modello, velocita_massima, cavalli):
		super().__init__(*args)
		self.modello, self.velocita_massima, self.cavalli = modello, velocita_massima, cavalli

	def fastest(self, rival):
		if max(self.velocita_massima, rival) == self.velocita_massima:
			print("la più veloce è la redbull!!")
		else:
			print("il rivale è più veloce")




def main():

	# basicCar = Auto("verde", 100000, 4, 2010)
	# basicCar2 = Auto("verde", 10050, 3, 2009)

	myCar = Ferrari("verde", 100000, 4, 2010, modello="original", velocita_massima=300, cavalli=5000)
	my2ndCar = Mercedes("verde", 100000, 4, 2010, modello="ciotta", velocita_massima=289, cavalli=3000)

	myCar.fastest(my2ndCar.velocita_massima)
	my2ndCar.fastest(myCar.velocita_massima)

	print(myCar)
main()
