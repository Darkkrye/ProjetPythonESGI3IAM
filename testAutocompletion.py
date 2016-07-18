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
from urllib.request import urlopen
import json

# POUR TESTER : 1er input => 2714 (double clic sur le bon dans la liste) / 2ème input => r (double clic sur n'importe lequel dans la liste

response = urlopen("https://gist.githubusercontent.com/Darkkrye/f69af450328241820083b311cd654641/raw/83294d623756be064399390305833e386c168f7d/frenchPostalCodes.json")
string = response.read().decode('utf-8')
json_obj = json.loads(string)

postalCodes = []
for x in range(0, len(json_obj)):
    postalCodes.append(json_obj[x]["codePostal"])

class AutocompleteEntry(Entry):
    def __init__(self, lista, isPostalCode, *args, **kwargs):
        
        Entry.__init__(self, *args, **kwargs)
        self.lista = lista
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        
        self.lb_up = False

    def changed(self, name, index, mode):  

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True
                
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            if isPostalCode(self.lb.get(ACTIVE)):
                test(self.lb.get(ACTIVE))
            else:
                print("Vous avez sélectionné : ", self.lb.get(ACTIVE).capitalize())
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]

def test(value):
    url = "http://vicopo.selfbuild.fr/cherche/" + value
    cities_response = urlopen(url)
    cities_string = cities_response.read().decode('utf-8')
    cities_obj = json.loads(cities_string)

    cities = []
    for x in range(0, len(cities_obj["cities"])):
        cities.append(cities_obj["cities"][x]["city"].lower())
        
    entry = AutocompleteEntry(cities, False, root)
    entry.grid(row=0, column=5)

def isPostalCode(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    root = Tk()
    root.geometry("1000x500")

    entry = AutocompleteEntry(postalCodes, True, root)
    entry.grid(row=0, column=0)

    root.mainloop()
