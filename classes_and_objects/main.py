#qui richiameremo la classe studente per creare un oggetto
#utilizzando appunto i dati di studente
#la classe definisce che cos'è l'oggetto è la rappresentazione
#digitale
#from file importa classe
from student import Student

student1 = Student("Carlo", "Business", 3.1, False)
student2 = Student("Sofia", "Mathematics", 3.5, True)
print(student1.name)
print(student2.major)
