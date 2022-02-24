import tkinter
from tkinter import ttk
import random
from ttkthemes import ThemedStyle
import requests
from bs4 import BeautifulSoup
import urllib.request
import PIL.ImageTk
import PIL.Image
from pyowm import OWM
from tkinter import *


def move_app(e):
    window.geometry(f'+{e.x_root}+{e.y_root}')
def quitter(e):
    window.quit()
def soup(city):
    url = "https://unsplash.com/s/photos/" +city+ "-skyline"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # print(soup.prettify())
    image_tags = soup.find_all('img')
    links = []
    for image_tag in image_tags:
        links.append(image_tag['src'])
    #print(len(links))
    return links

def clicked():
    global background
    global symbol
    res = txt.get()
    city = res.capitalize()
    links = soup(city)
    urllib.request.urlretrieve(links[random.randint(8,50)], "city.jpg")
    background = PIL.ImageTk.PhotoImage(PIL.Image.open(r"city.jpg"))
    canvas.itemconfig(back, image=background, anchor=NW)

    location = mgr.weather_at_place(city)
    weather = location.weather
    temp = weather.temperature('celsius')
    temps = list(temp.values())


    if weather.detailed_status == 'broken clouds' or weather.detailed_status == 'few clouds' or weather.detailed_status == 'scattered clouds':
        symbol = "\u2601\n"
    if weather.detailed_status == 'clear sky':
        symbol = "\u2600"
    if weather.detailed_status.find("rain"):
        symbol = "\U0001f327"
    if weather.detailed_status == 'snow':
        symbol = "\u2744"
    if weather.detailed_status == 'thunderstorm':
        symbol = "\U0001f329"
    if weather.detailed_status == 'mist':
        symbol = "\U0001f32b"

    title_label.config(text=symbol.strip() + "Weather App" )
    canvas.itemconfig(text,text="\n{}\n\n{}°\n{} {}\n\nHigh of {}°\nLow of {}°".format(city, round(temps[0]),
                                                                                 weather.detailed_status,symbol, round(temps[1]),
                                                                                 round(temps[2])), font=("San-Fransisco 17 "), fill="white", justify=CENTER )






if __name__ == "__main__":
    API = 'ad6b6ea3087ec42653205b0c23fa7f10'
    owm = OWM(API)
    mgr = owm.weather_manager()
    window = tkinter.Tk()
    style = ThemedStyle(window)
    style.set_theme('equilux')
    window.configure(background="#3d3d3d")
    window.title("Weather App")
    window.geometry('340x400')
    window.maxsize(340, 400)

    # remove title bar
    window.overrideredirect(True)
    title_bar = Frame(window, bg="#3d3d3d", relief="raised", bd=0)
    title_bar.pack(expand=1, fill=X)
    # Bind the titlebar
    title_bar.bind("<B1-Motion>", move_app)

    # Create title text
    symbol = "\u2600"
    title_label = Label(title_bar, text= symbol + "Weather App", bg="#3d3d3d", fg="white")
    title_label.pack(side=LEFT, pady=4)

    # Create close button on titlebar
    close_label = Label(title_bar, text="  X    ", bg="#3d3d3d", fg="white", relief="sunken", bd=0)
    close_label.pack(side=RIGHT, pady=4)
    close_label.bind("<Button-1>", quitter)

    # Create canvas
    canvas = Canvas(window,width=200,height=330)
    canvas.pack(fill = "both",expand=True)
    background = PIL.ImageTk.PhotoImage(PIL.Image.open(r"city1.jpg"))
    back = canvas.create_image(0,0,image=background,anchor=NW)
    # Create text field
    text= canvas.create_text(170, 150, text="         Welcome \n\n       Instructions:\n\n1.Enter a city name.\n\n2.Press the button.", font=("San-Fransisco",15), fill="white")
    txt = ttk.Entry(window, width=32)
    txt.pack(side=LEFT, padx=14)
    txt.focus()
    # Create Button
    btn = ttk.Button(window,text="Go!" ,command= lambda :clicked())
    btn.pack(side=RIGHT, padx=14)

    window.mainloop()

