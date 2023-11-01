#i dizionari sono delle parole chiave
#che possono essere usate per definire dei significati
#utilizziamo un a 'key' e gli diamo un valore
#le key non possono essere duplicate
month_convertions = {
	"Gen": "Gennaio",
	"Feb": "Febbraio",
	"Mar": "Marzo",
	"Apr": "Aprile",
	"Mag": "Maggio",
	"Giu": "Giugno",
	"Lug": "Luglio",
	"Ago": "Agosto",
	"Set": "Settembre",
	"Ott": "Ottobre",
	"Nov": "Novembre",
	"Dic": "Dicembre"
}

print(month_convertions["Feb"])
print(month_convertions.get("Nov"))
#se dobbiamo passare un valore di default
#dobbiamo fare una cosa del genere
print(month_convertions.get("Wrong","Inserire uno dei valori nel dizionario"))
