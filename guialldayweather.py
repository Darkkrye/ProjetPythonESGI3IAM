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
class GUIAllDayWeather():

    def __init__(self, all_day_weather, main):

        canvas = Canvas(main, width=250, height=400, background="white")
        canvas.pack(side='left', fill='x', expand='yes')
        self.cv = canvas

        i_a_d = []
        i_d_d_d = []
        i_d_d_e = []

        for i in range(0, len(all_day_weather)):
            adw = all_day_weather[i]
            #raw_data = urlopen(adw.icon_url).read()
            #im = Image.open(BytesIO(raw_data))
            #i_a_d.append(ImageTk.PhotoImage(im))

            #canvas = Canvas(main, width=250, height=400)
            #canvas.pack(side=LEFT, fill=X, expand=YES)

            image_byt = urlopen(adw.icon_url).read()
            image_b64 = base64.encodestring(image_byt)
            i_a_d.insert(i, PhotoImage(data=image_b64))

            rectangle = self.cv.create_rectangle((i+1) * 245, 390, 20, 20)

            #self.cv.bind("<Enter>", self.on_enter)
            #cv.bind("<Leave>", self.on_leave)

            
##            rectangle = self.cv.create_rectangle(10, 25, 225, 400, fill="#3131ce")
##            self.cv.create_image(100,25, image=i_a_d[i], anchor='nw')
##            
##            date = adw.day_name + " " + str(adw.day_date) + " " + adw.month_name + " " + str(adw.year_date) + " (" + str(adw.day_date) + "/" + str(adw.month_date) + "/" + str(adw.year_date) + ")"
##            self.cv.create_text(120, 100, text=date, fill="white")
##
##            temperature = "Temperature (max/min): " + str(adw.max_temp) + "°C / " + str(adw.min_temp) + "°C"
##            self.cv.create_text(120, 125, text=temperature, fill="white")
##
##            self.cv.create_text(120, 150, text=adw.description, fill="white")
##
##            max_wind = "Vent max (vit/dir): " + str(adw.max_wind_speed) + "km/h / " + adw.max_wind_dir
##            ave_wind = "Vent moyen (vit/dir): " + str(adw.ave_wind_speed) + "km/h / " + adw.ave_wind_dir
##            self.cv.create_text(120, 175, text=max_wind, fill="white")
##            self.cv.create_text(120, 200, text=ave_wind, fill="white")
##
##            if adw.max_hum == 0 and adw.min_hum == 0:
##                hum = "Humidité : " + str(adw.ave_hum) + "%"
##            else:
##                hum = "Humidité (max/min) : " + str(adw.max_hum) + "%/" + str(adw.min_hum) + "%"
##            self.cv.create_text(120, 225, text=hum, fill="white")
            
            
    def on_enter(self, event):
        cv.itemconfig(rectangle, fill='red')
        print("Test")

    def on_leave(self, enter):
        cv.itemconfig(rectangle, fill='blue')
        print("Test2")
