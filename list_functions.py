#funzioni utilizzabili per le liste
lucky_numbers = [4, 2, 7, 9, 42, 10]
numbers = [7, 2, 33, 10, 77, 1]
friends = ["Dario", "Lorenzo", "Osema", "Piero", "Giuseppe"]
#funzione extends prende una lista e l'attacca a quella specificata
friends.extend(lucky_numbers)
#si possono anche aggiungere eleminti singoli da una lista all'altra
#stampa dei valori
friends.append("Aggiunta")
print(friends)
#la funzione insert inserisce un valore nell'indice specificato
#facendo scalare gli altri valori dopo
lucky_numbers.insert(1, "Pierpaolo")
print(lucky_numbers)
lucky_numbers.remove("Pierpaolo")
print(lucky_numbers)
#cancella tutti i valori in una lista
lucky_numbers.clear()
#elimino un elemento dalla mia lista
friends.pop(2)
#c'è anche un modo per controllare se unvalore ricercato è
#all'interno della nostra lista
print(friends.index("Lorenzo")) #se il valore non è presente da errore
#la funzione count mi dice quante volte un valore compare nella lista
print(friends.count("Dario"))
#ordino la lista
numbers.sort()
print(numbers)
#ordino al contrario
numbers.reverse()
#Copio una lista
friends2 = friends.copy()
print(friends2)
