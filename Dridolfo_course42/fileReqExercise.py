import os
import requests


def writeRequest():
    f = open("gottenRequest.html","w")
    res = requests.get("https://google.com")
    f.write(res.text) #per la conversione e formattazione

def dRidolfoWay():
    res = requests.get("https://google.com")

    with open("file.html", "w") as f:
        f.write(res.text)

def takeInfo():
    #https://crumb.sh/F65R4QZRHmo
    if "python" in requests.get("https://crumb.sh/F65R4QZRHmo").text.lower():
        print("si")
    else:
        print("no")

def modify():
    test = requests.post("https://www.w3schools.com/python/demopage.php", json={"key": "value"})

    print(test.status_code, test.reason, test.text)


#writeRequest()
#takeInfo()
modify()

#estrarre i dati da una pagina html prossimo compito