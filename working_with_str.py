#\n da andare a capo in un solo print
phrase = "Una stringa in una variabile"
print("Vado\na capo")
print("stampo una virgoletta \"")
#con l'escape che sarebbe lo \ puoi stampare
#buona parte dei valori che non sarebbero printabili
print("Qui ho "+ phrase)
#c'è anche una concatenazione che sarebbe aggiungere con il +
#una strigna ad un'altra
print(phrase +"che è stata concatenata")
#posso utilizzare funzioni già esistenti per manipolare la mia
#stringa, per maggiori info guarda le funzioni in questione
print(phrase.upper())
print(phrase.isupper()) #stampa true se la  variabile è tutta in stampatello
#puoi anche mischiare più funzioni insieme una dietro l'altra
print(phrase.upper().isupper())
#la lunchezza della variabile
print(len(phrase)) #sta volta la funzione ha bisogno di un contenuto
#voglio sapere che carattere c'è in posizione x
print(phrase[1]) #conta il valore 0 va da 0 a len(phrase)
#voglio sapere in quale location risiede la mia stringa
print("La v nella frase "+ phrase +" riside all'indice", phrase.index("v"))
#funziona anche con le parole
#puoi usare la funzione replace per cambiare le stringhe
print(phrase.replace("in una variabile", "cambiata"))
