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
        self.all_day_weather = all_day_weather
        self.detailed_day_weather = detailed_day_weather

        canvas = Canvas(main, width=250, height=400, background="white")
        canvas.pack(side='left', expand='yes')
        self.cv1 = canvas
        self.cv1.bind("<Enter>", self.on_enter1)
        self.cv1.bind("<Leave>", self.on_leave1)
        self.cvs.append(self.cv1)
        canvas2 = Canvas(main, width=250, height=400, background="white")
        canvas2.pack(side='left', expand='yes')
        self.cv2 = canvas2
        self.cv2.bind("<Enter>", self.on_enter2)
        self.cv2.bind("<Leave>", self.on_leave2)
        self.cvs.append(self.cv2)
        canvas3 = Canvas(main, width=250, height=400, background="white")
        canvas3.pack(side='left', expand='yes')
        self.cv3 = canvas3
        self.cv3.bind("<Enter>", self.on_enter3)
        self.cv3.bind("<Leave>", self.on_leave3)
        self.cvs.append(self.cv3)
        canvas4 = Canvas(main, width=250, height=400, background="white")
        canvas4.pack(side='left', expand='yes')
        self.cv4 = canvas4
        self.cv4.bind("<Enter>", self.on_enter4)
        self.cv4.bind("<Leave>", self.on_leave4)
        self.cvs.append(self.cv4)

        self.fillWithData()
            

    def fillWithData(self):
        i_a_d = []

        for i in range(0, len(self.all_day_weather)):
            adw = self.all_day_weather[i]
            canvas = self.cvs[i]
            
            image_byt = urlopen(adw.icon_url).read()
            image_b64 = base64.encodestring(image_byt)
            i_a_d.insert(i, PhotoImage(data=image_b64))
            
            rectangle = canvas.create_rectangle(10, 25, 225, 400, fill="#3131ce")
            canvas.create_image(100,25, image=i_a_d[i], anchor='nw')
            
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

    def fillWithData2(self):
        
            
    def on_enter1(self, event):
        rectangle = self.cv1.create_rectangle(10, 25, 225, 400, fill="red")

    def on_leave1(self, enter):
        rectangle = self.cv1.create_rectangle(10, 25, 225, 400, fill="#3131ce")
        self.fillWithData()

    def on_enter2(self, event):
        rectangle = self.cv2.create_rectangle(10, 25, 225, 400, fill="red")

    def on_leave2(self, enter):
        rectangle = self.cv2.create_rectangle(10, 25, 225, 400, fill="#3131ce")
        self.fillWithData()

    def on_enter3(self, event):
        rectangle = self.cv3.create_rectangle(10, 25, 225, 400, fill="red")

    def on_leave3(self, enter):
        rectangle = self.cv3.create_rectangle(10, 25, 225, 400, fill="#3131ce")
        self.fillWithData()

    def on_enter4(self, event):
        rectangle = self.cv4.create_rectangle(10, 25, 225, 400, fill="red")

    def on_leave4(self, enter):
        rectangle = self.cv4.create_rectangle(10, 25, 225, 400, fill="#3131ce")
        self.fillWithData()
