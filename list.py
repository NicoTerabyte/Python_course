#27 ottobre 2023
#le liste possono contenere ogni valore
#example = [5, "nome", True]
friends = ["Dario", "Lorenzo", "Osema", "Piero", "Giuseppe"]
print(friends) #Stampa tutta la lista
#stampiamo un valore singolo partendo da 0
print(friends[0]) #i numeri negativi vengonpo gestiti al contrario
#per esempio se mettessi -1 andrai all'ultimo elemento
#caso in cui voglio stampare da valore n in poi
print(friends[1:])
#printo un range di valori
print(friends[1:3])
#si può cambiare ovviamente il valore in una posizione specificata
friends[2] = "Venelin"
