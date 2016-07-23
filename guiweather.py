import sys
try:
    # for Python2
    from Tkinter import *  ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *  ## notice here too
import re
import io
import base64

import autocompleteentry as ace
import modelDetailedDayWeather as mddw
import modelAllDayWeather as madw

from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
from urllib.request import urlopen

import json
class GUIWeather():

    def __init__(self, detailed_day_weather, all_day_weather, main):

        self.cvs = []
        self.images1 = []
        self.images2 = []
        self.images3 = []
        self.all_day_weather = all_day_weather
        self.detailed_day_weather = detailed_day_weather

        canvas = Canvas(main, width=250, height=400)
        canvas.pack(side='left', expand='yes')
        self.cv1 = canvas
        self.cv1.bind("<Enter>", self.on_enter1)
        self.cv1.bind("<Leave>", self.on_leave1)
        self.cvs.append(self.cv1)
        canvas2 = Canvas(main, width=250, height=400)
        canvas2.pack(side='left', expand='yes')
        self.cv2 = canvas2
        self.cv2.bind("<Enter>", self.on_enter2)
        self.cv2.bind("<Leave>", self.on_leave2)
        self.cvs.append(self.cv2)
        canvas3 = Canvas(main, width=250, height=400)
        canvas3.pack(side='left', expand='yes')
        self.cv3 = canvas3
        self.cv3.bind("<Enter>", self.on_enter3)
        self.cv3.bind("<Leave>", self.on_leave3)
        self.cvs.append(self.cv3)
        canvas4 = Canvas(main, width=250, height=400)
        canvas4.pack(side='left', expand='yes')
        self.cv4 = canvas4
        self.cv4.bind("<Enter>", self.on_enter4)
        self.cv4.bind("<Leave>", self.on_leave4)
        self.cvs.append(self.cv4)

        for i in range(0, len(self.all_day_weather)):
            image_byt = urlopen(self.all_day_weather[i].icon_url).read()
            image_b64 = base64.encodestring(image_byt)
            self.images1.append(PhotoImage(data=image_b64))

        for i in range(0, len(self.detailed_day_weather)):
            image_byt = urlopen(self.detailed_day_weather[i].day_icon_url).read()
            image_b64 = base64.encodestring(image_byt)
            self.images2.append(PhotoImage(data=image_b64))

        for i in range(0, len(self.detailed_day_weather)):
            image_byt = urlopen(self.detailed_day_weather[i].eve_icon_url).read()
            image_b64 = base64.encodestring(image_byt)
            self.images3.append(PhotoImage(data=image_b64))

        self.fill_with_data(self.cv1, 0)
        self.fill_with_data(self.cv2, 1)
        self.fill_with_data(self.cv3, 2)
        self.fill_with_data(self.cv4, 3)
            

    def fill_with_data(self, canvas, i):
        for i in range(0, len(self.all_day_weather)):
            adw = self.all_day_weather[i]
            canvas = self.cvs[i]
            
            rectangle = canvas.create_rectangle(10, 25, 225, 400, fill="#3131CE")
            
            canvas.create_image(100, 25, image=self.images1[i], anchor='nw')
            
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


    def fill_with_data2(self, canvas, i):
        adw = self.all_day_weather[i]
        ddw = self.detailed_day_weather[i]
        
        rectangle = canvas.create_rectangle(10, 25, 225, 400, fill="#3180CE")

        date = adw.day_name + " " + str(adw.day_date) + " " + adw.month_name + " " + str(adw.year_date) + " (" + str(adw.day_date) + "/" + str(adw.month_date) + "/" + str(adw.year_date) + ")"
        canvas.create_text(120, 35, text=date, fill="white")
        
        canvas.create_image(100,50, image=self.images2[i], anchor='nw')

        canvas.create_text(120, 125, text=ddw.day_title, fill="white")
        day_description = ddw.day_description.replace(". ", ".\r")
        canvas.create_text(120, 160, text=day_description, fill="white")

        canvas.create_image(100,200, image=self.images3[i], anchor='nw')

        canvas.create_text(120, 275, text=ddw.eve_title, fill="white")
        evening_description = ddw.eve_description.replace(". ", ".\r")
        canvas.create_text(120, 310, text=evening_description, fill="white")

            
    def on_enter1(self, event):
        self.fill_with_data2(self.cv1, 0)

    def on_leave1(self, enter):
        self.fill_with_data(self.cv1, 0)

    def on_enter2(self, event):
        self.fill_with_data2(self.cv2, 1)

    def on_leave2(self, enter):
        self.fill_with_data(self.cv2, 1)

    def on_enter3(self, event):
        self.fill_with_data2(self.cv3, 2)
        
    def on_leave3(self, enter):
        self.fill_with_data(self.cv3, 2)

    def on_enter4(self, event):
        self.fill_with_data2(self.cv4, 3)

    def on_leave4(self, enter):
        self.fill_with_data(self.cv4, 3)
