#qui scriveremo in un file
#faremo anche un po' di appending
#funzione write scriamo nel file che abbiamo aperto
#Tenere nota del fatto che se il faile non ha una newline
#la scritta verrà appesa subito dopo la parola precedente nel suddetto file
#per evitare questo problema ci sarà il bisogno di utilizzare il carettere speciale prima
#di scrivere
#con la scrittura (modalità w) bisogna fare attenzione peché il file aperto in scrittura
#verrà sovrascritto
#sempre con questa modalità però possiamo creare un nuovo file
team_file = open("index.html", "w")

# team_file.write("\ndullmember")
team_file.write("<p>THIS IS A HTML FILE</p>")
team_file.close()
