#import serve per la manipolazione dei file
import os
import sys
import requests

#esistono varie flag per leggere e scrivere nei file ('r', 'w', 'a') a sta per append
#con with puoi chiudere i file in automatico alla fine dello scope
#cioè del blocco del with, è praticamente un while
#with open("exClass.py", "a") as f:
 #   print(f.read())
def scraperino():
    #post per modificare un sito
    res = requests.get("https://example.com")
    #res.status_code, res.text, res.content, res.reason parti più importanti da reperire quando
    #si usa request: code(status della richiesta) text(il contenuto della risposta)
    #content(la risposta stessa) reason(lo status della risposta)
    print(res.status_code, res.text, res.content, res.reason)


scraperino()