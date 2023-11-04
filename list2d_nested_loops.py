#lavoreremo con liste 2D e loop innestati
#qui abbiamo una lista duedimensionale con altre liste al suo interno
#la lista possiede 4 righe e 3 colonne
number_grid = [
	[1, 2, 3],
	[90, 95, 100],
	[7, 14, 21],
	[0]
]
#stampiamo alcuni valori
#(la riga 0 è quella con 1, 2, 3 la colonna 0 è 1)
print(number_grid[0][0]) #in questo caso stamperemo il valore nella riga 0 colonna 0

#faremo un loop innestato per stampare tutta la lista
for row in number_grid:
	for column in row:
		print(column)
		if column == 7:
			print("Lucky Number appeared!")
