#!/usr/bin/python3.4
# -*-coding:Utf-8 -*
import sys
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice here too
import re
import autocompleteentry as ace
from urllib.request import urlopen
import json

# POUR TESTER : 1er input => 2714 (double clic sur le bon dans la liste) / 2ème input => r (double clic sur n'importe lequel dans la liste

response = urlopen("https://gist.githubusercontent.com/Darkkrye/f69af450328241820083b311cd654641/raw/83294d623756be064399390305833e386c168f7d/frenchPostalCodes.json")
string = response.read().decode('utf-8')
json_obj = json.loads(string)

postalCodes = []
for x in range(0, len(json_obj)):
    postalCodes.append(json_obj[x]["codePostal"])

def onPostalCodeSelected(value):
    url = "http://vicopo.selfbuild.fr/cherche/" + value
    cities_response = urlopen(url)
    cities_string = cities_response.read().decode('utf-8')
    cities_obj = json.loads(cities_string)

    cities = []
    for x in range(0, len(cities_obj["cities"])):
        cities.append(cities_obj["cities"][x]["city"].lower())
        
    entry = ace.AutocompleteEntry(cities, main)
    entry.grid(row=0, column=5)

def onCitySelected(value):
    print("Vous avez sélectionné : ", value)

ace.onPostalCodeSelected = onPostalCodeSelected
ace.onCitySelected = onCitySelected

if __name__ == '__main__':
    main = Tk()
    main.title("Pythéo")
    main.geometry("1000x500")

    entry = ace.AutocompleteEntry(postalCodes, main)
    entry.grid(row=0, column=0)

    main.mainloop()
