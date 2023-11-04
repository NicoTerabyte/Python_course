#leggiamo un file con python
#con la funzione file apriamo il suddetto file
#la funzione accetta il file in questione e la modalità di apertura
#per modalità si intende come apriamo il file
#se è leggibile o posso modificarlo ecc
#r (lettura), w(scrittura), a(append) mettiamo roba extra nel file
#r+ puoi sia leggere che scrivere
#ogni volta che apri un file ad una certa bisogna sempre chiuderlo
team_file = open("file", "r") #r significa che saremo in lettura
#la funzione readable ci dice se il file è leggibile o no (con True o False)
#la funzione read si limita a leggere il file
#readline legge una riga del file la prossima volta che verrà
#chiamata leggerà la riga successiva
#con readlines salviamo i valori del file in una lista
#print(team_file.read())
print(team_file.readline())
#print(team_file.readlines()[1])
for team in team_file.readlines():
	print(team)
team_file.close()
