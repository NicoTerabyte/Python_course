#i for lavorano in una maniera particolare
#qua i for funzinano in maniera particolare
#in questo caso io faccio così:
#per ogni lettera in test ne stampo una
#questo concetto è molto astratto perché
#in questo caso abbiamo creato un'array chiamato friends
#che al suo interno ha tre variabili da quel che ho capito nel for
#noi letteralmente creiamo una variabile d'appoggio per l'array o per
#qualunque cosa vogliamo scorrere un valore alla volta
# e cerchiamo di dargli una logica qui, per esempio diciamo stampami un friend
#alla volta nella mia lista di friends per dire friend è un nome a caso logicamente
#collegato alla variabile friends
friends = ["piero", "carlo", "gianni"]
for friend in friends:
	print(friend)

#esempio con i numero
for index in range(14):
	print(index) #parte da 0 a 13

for index in range(3, 14):
	print(index) #parte da 0 a 13 (non conta l'ultimo)

#altro esempio mischiando l'indice all'array friends
for index in range(len(friends)):
	print(friends[index])
