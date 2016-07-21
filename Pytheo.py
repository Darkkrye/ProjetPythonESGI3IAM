#!/usr/bin/python3.4
# -*-coding:Utf-8 -*
import sys
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice here too
from tkinter import messagebox
import re
import autocompleteentry as ace
import modelDetailedDayWeather as mddw
import modelAllDayWeather as madw
import guialldayweather as gadw

from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
from urllib.request import urlopen

import json

# - CONSTANTS
WG_KEY = "e9cf1566c008b39f"
IS_ALREADY_PASSED = True

# - REDEFINE FUNCTIONS
# Functions
def onZipCodeSelected(value):
    url = "http://vicopo.selfbuild.fr/cherche/" + value
    cities_response = urlopen(url)
    cities_string = cities_response.read().decode('utf-8')
    cities_obj = json.loads(cities_string)

    cities = []
    for x in range(0, len(cities_obj["cities"])):
        cities.append(cities_obj["cities"][x]["city"].capitalize())

    label = Label(cadre, text="Puis la ville :").pack(side="top", fill=X)
    entry = ace.AutocompleteEntry(cities, cadre).pack(side="top", fill=Y)

def onCitySelected(value):
    if "-" in value:
        value = value.split("-", 1)[0]
        print(value)
    url = "http://api.wunderground.com/api/" + WG_KEY + "/forecast/lang:FR/q/France/" + value + ".json"
    print(url)
    weather_response = urlopen(url)
    weather_string = weather_response.read().decode('utf-8')
    weather_json_obj = json.loads(weather_string)

    detailed_day_weather = []
    all_day_weather = []

    try:
        if weather_json_obj["response"]["error"]:
            messagebox.showinfo("Erreur", "Aucune météo trouvée pour cette ville.")
    except:
        for i in range(0, len(weather_json_obj["forecast"]["txt_forecast"]["forecastday"]), 2):
            day = weather_json_obj["forecast"]["txt_forecast"]["forecastday"][i]
            evening = weather_json_obj["forecast"]["txt_forecast"]["forecastday"][i+1]
            weather = mddw.DetailedDayWeather(day["icon_url"], day["title"].capitalize(), day["fcttext_metric"], evening["icon_url"], evening["title"].capitalize(), evening["fcttext_metric"])
            detailed_day_weather.append(weather)

        for j in range(0, len(weather_json_obj["forecast"]["simpleforecast"]["forecastday"])):
            day = weather_json_obj["forecast"]["simpleforecast"]["forecastday"][j]
            weather = madw.AllDayWeather(day["date"]["day"], day["date"]["weekday"].capitalize(), day["date"]["month"], day["date"]["monthname"].capitalize(), day["date"]["year"], day["high"]["celsius"], day["low"]["celsius"], day["conditions"], day["icon_url"], day["maxwind"]["kph"], day["maxwind"]["dir"], day["avewind"]["kph"], day["avewind"]["dir"], day["maxhumidity"], day["minhumidity"], day["avehumidity"])
            all_day_weather.append(weather)

    gadw.GUIAllDayWeather(all_day_weather, main)

# Setting redefinitions
ace.onZipCodeSelected = onZipCodeSelected
ace.onCitySelected = onCitySelected


# - PRE-LAUNCH CODE :
# Get all zip codes
response = urlopen("https://gist.githubusercontent.com/Darkkrye/f69af450328241820083b311cd654641/raw/ffeeb16776565a8dd612f0ec076f1946d0e5b4aa/frenchZipCodes.json")
string = response.read().decode('utf-8')
json_obj = json.loads(string)

zipCodes = []
for x in range(0, len(json_obj)):
    zipCodes.append(json_obj[x]["codePostal"])


# - LAUNCH CODE
if __name__ == '__main__':
    main = Tk()
    main.title("Pythéo")
    main.geometry("1000x600")

    cadre = Frame(main, width=768, height=576, borderwidth=1)
    cadre.pack(fill=BOTH)

    Label(cadre, text="Bienvenue dans Pythéo").pack(side="top", fill=X)

    Label(cadre, text="Veuillez sélectionner le Code Postal :").pack(side="top", fill=X)
    entry = ace.AutocompleteEntry(zipCodes, cadre).pack(side="top", fill=Y)

    main.mainloop()



# POUR TESTER : 1er input => 2714 (double clic sur le bon dans la liste) / 2ème input => r (double clic sur n'importe lequel dans la liste
