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
import modelDetailedDayWeather as mddw
import modelAllDayWeather as madw

from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
from urllib.request import urlopen

import json

detailed_day_weather = []
all_day_weather = []

detailed_day_weather.append(mddw.DetailedDayWeather("http://icons.wxug.com/i/c/k/chancetstorms.gif", "Mercredi", "Ciel partiellement nuageux avec risque d'orage. Très chaud. Maximales : 33 °C. Vents ENE soufflant de 10 à 15 km/h. Risque de pluie : 30 %.", "http://icons.wxug.com/i/c/k/nt_chancetstorms.gif", "Mercredi Soir", "Orages épars. Minimales : 18 °C. Vents SSO et variables. Risque de pluie : 60 %."))
detailed_day_weather.append(mddw.DetailedDayWeather("http://icons.wxug.com/i/c/k/partlycloudy.gif", "Jeudi", "Partiellement nuageux. Maximales : 32 °C. Vents OSO et variables.", "http://icons.wxug.com/i/c/k/nt_chancetstorms.gif", "Jeudi Soir", "Ciel partiellement nuageux avec risque d'orage. Minimales : 16 °C. Vents NO et variables. Risque de pluie : 30 %."))
detailed_day_weather.append(mddw.DetailedDayWeather("http://icons.wxug.com/i/c/k/chancetstorms.gif", "Vendredi", "Orages épars. Maximales : 29 °C. Vents N soufflant de 10 à 15 km/h. Risque de pluie : 50 %.", "http://icons.wxug.com/i/c/k/nt_clear.gif", "Vendredi Soir", "Orages épars. Maximales : 29 °C. Vents N soufflant de 10 à 15 km/h. Risque de pluie : 50 %."))
detailed_day_weather.append(mddw.DetailedDayWeather("http://icons.wxug.com/i/c/k/clear.gif", "Samedi", "Ciel plutôt dégagé. Maximales : 28 °C. Vents NNO soufflant de 10 à 15 km/h.", "http://icons.wxug.com/i/c/k/nt_clear.gif", "Samedi Soir", "Ciel plutôt dégagé. Minimales : 14 °C. Vents N soufflant de 10 à 15 km/h."))

all_day_weather.append(madw.AllDayWeather(20, "Mercredi", 7, "Juillet", 2016, 33, 18, "Risque d'orage", "http://icons.wxug.com/i/c/k/chancetstorms.gif", 16, "ENE", 13, "ENE", 0, 0, 45))
all_day_weather.append(madw.AllDayWeather(21, "Jeudi", 7, "Juillet", 2016, 32, 16, "Partiellement nuageux", "http://icons.wxug.com/i/c/k/partlycloudy.gif", 16, "OSO", 10, "OSO", 0, 0, 59))
all_day_weather.append(madw.AllDayWeather(22, "Vendredi", 7, "Juillet", 2016, 29, 15, "Risque d'orage", "http://icons.wxug.com/i/c/k/chancetstorms.gif", 24, "N", 16, "N", 0, 0, 63))
all_day_weather.append(madw.AllDayWeather(23, "Samedi", 7, "Juillet", 2016, 28, 14, "Ciel dégagé", "http://icons.wxug.com/i/c/k/clear.gif", 24, "NNO", 16, "NNO", 0, 0, 57))

# - LAUNCH CODE
if __name__ == '__main__':
    main = Tk()
    main.title("testGUI")
    main.geometry("1000x600")

    cadre = Frame(main, width=768, height=576, borderwidth=1)
    cadre.pack(fill=BOTH)

    Label(cadre, text="Bienvenue dans Pythéo").pack(side="top", fill=X)

    i_a_d = []
    i_d_d_d = []
    i_d_d_e = []

    for i in range(0, len(all_day_weather)):
        adw = all_day_weather[i]
        raw_data = urlopen(adw.icon_url).read()
        im = Image.open(BytesIO(raw_data))
        i_a_d.append(ImageTk.PhotoImage(im))

        canvas = Canvas(cadre, width=250, height=400)
        canvas.create_rectangle(10, 25, 225, 400, fill="#3131ce")
        canvas.create_image(100,25, anchor=NW, image=i_a_d[i])
        print(i_a_d[i])
        
        date = adw.day_name + " " + str(adw.day_date) + " " + adw.month_name + " " + str(adw.year_date) + " (" + str(adw.day_date) + "/" + str(adw.month_date) + "/" + str(adw.year_date) + ")"
        canvas.create_text(120, 100, text=date, fill="white")

        temperature = "Temperature (max/min): " + str(adw.max_temp) + "°C / " + str(adw.min_temp) + "°C"
        canvas.create_text(120, 125, text=temperature, fill="white")

        canvas.create_text(120, 150, text=adw.description, fill="white")

        max_wind = "Vent max (vit/dir): " + str(adw.max_wind_speed) + "km/h / " + adw.max_wind_dir
        ave_wind = "Vent moyen (vit/dir): " + str(adw.ave_wind_speed) + "km/h / " + adw.ave_wind_dir
        canvas.create_text(120, 175, text=max_wind, fill="white")
        canvas.create_text(120, 200, text=ave_wind, fill="white")

        if adw.max_hum == 0 and adw.min_hum == 0:
            hum = "Humidité : " + str(adw.ave_hum) + "%"
        else:
            hum = "Humidité (max/min) : " + str(adw.max_hum) + "%/" + str(adw.min_hum) + "%"
        canvas.create_text(120, 225, text=hum, fill="white")
        
        canvas.pack(side=LEFT, fill=X)

##    for i in range(0, len(detailed_day_weather)):
##        weather = detailed_day_weather[i]
##        print(weather.day_icon_url, " / ", weather.day_title, " / ", weather.day_description, " / ", weather.eve_icon_url, " / ", weather.eve_title, " / ", weather.eve_description, "\n")
##
##        raw_data = urlopen(weather.day_icon_url).read()
##        im = Image.open(BytesIO(raw_data))
##        images1.append(ImageTk.PhotoImage(im))
##
##        raw_data2 = urlopen(weather.eve_icon_url).read()
##        im2 = Image.open(BytesIO(raw_data2))
##        images2.append(ImageTk.PhotoImage(im2))
##
##        canvas = Canvas(cadre, width=250, height=400)
##        canvas.create_rectangle(10, 25, 225, 400)
##        canvas.create_image(10,25, anchor = NW, image=images1[i])
##        canvas.create_image(175,25, anchor = NW, image=images2[i])
##        canvas.pack(side=LEFT, fill=X)
    

    main.mainloop()
