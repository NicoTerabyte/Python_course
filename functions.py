#creeremo e utilizzeremo una funzione
#per dichiarare una funzione si usa la parola chiave def
def	say_hi():
	print("hi")
#ora creiamo una funzione che prenda un argomento
#ps ne puoi mettere quanti ne vuoi
def	call_user(name):
	print("Hey "+ name)

#per eseguire la funzione ovviamente bisogna richiamarla
say_hi()
name = input("put your name ")
call_user(name)
