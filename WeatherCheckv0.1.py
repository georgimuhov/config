import os
import sys
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import *
import requests

#Main Window
window = Tk()
window.title("Weather v0.1")
window.geometry("200x120")
window.eval("tk::PlaceWindow . center")
window.resizable(False, False)
window.attributes("-alpha", 0.91)

icon = os.path.join(sys.path[0], "icon.ico")
window.iconbitmap(icon)
#window['bg'] = '#FFFFFF'

def check_weather():
	
	city = textbox.get()
	key = '6c6729e6d8d43230732b20cc42b45e8c'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': key, 'q': city, 'units': 'metric'}
	result = requests.get(url, params=params)
	weather = result.json()
	label1["text"] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
	label1["text"] = label1["text"]+str("°C")

def about():
	messagebox.showinfo("About", "Created by 6l4br10n!")
	 
#Menü
menubar = Menu(window)
window.config(menu=menubar)
#Undermenü
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=window.destroy)

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=about)

#Hauptmenü
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Help", menu=help_menu)

#Button
button1 = ttk.Button(window, text="Check the Weather", command=check_weather)
button1.place (x=30, y=37, width=145)
button1.bind("<ButtonRelease-1>")

#TextBox
textbox = ttk.Entry(window, justify="center")
textbox.insert(0, "München")
textbox.place (x=10, y=12, width=180)

#InfoLabel 
label1 = ttk.Label(window, text=" ", font=19)
label1.place (x=50, y=65)

window.mainloop()


