import requests as re
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
def get_ip():

    response = re.get('https://ipinfo.io')
    public_ip = response.text.strip()
    ip = public_ip.split()[2][1:-3]
    return ip

api_key = "d19cccf00c602098033b2e97309cc6f7"

endpoint = f'http://api.weatherstack.com/current'


root = tk.Tk()
root.geometry("800x599")
root.resizable(width=False, height=False)

img = Image.open('weather.jpg')
background_image = ImageTk.PhotoImage(image=img)
label = tk.Label(root, image=background_image)
label.place(relwidth=1, relheight=1)



country_entry_label = tk.Label(root, text="Country", font=("Arial", 20), bg="#5F9AD2")
country_entry_label.place(x=75, y=5)

country = tk.StringVar()

country_entry = tk.Entry(root, bg='#70A7D8', font=("Arial", 20), textvariable=country)
country_entry.place(x=30, y=50, height=50, width=200)

def get_weather_info(query) -> dict:
    api_key = "d19cccf00c602098033b2e97309cc6f7"

    endpoint = f'http://api.weatherstack.com/current'

    params = {
        'access_key':api_key,
        'query':query
    }

    respons = re.get(endpoint, params=params)

    data = respons.json()

    location = data['location']['name']
    country = data['location']['country']
    weather_descriptions = data['current']['weather_descriptions'][0]
    temperature = data['current']['temperature']
    wind_speed = data['current']['wind_speed']
    wind_direction = data['current']['wind_dir']
    humidity = data['current']['humidity']
    feels_like = data['current']['feelslike']

    return {
        "location":location,
        "country":country,
        "weather_descriptions":weather_descriptions,
        "temperature":temperature,
        "wind_speed":wind_speed,
        "wind_direction":wind_direction,
        "humidity":humidity,
        "feels_like":feels_like

    }



def display_whaether_info(info_dect:dict):
    
    location_label = tk.Label(root, text=info_dect["location"], width=10, font=('forte', 60), bg='#4583B4', fg='blue')
    location_label.place(x=290, y=10)

    temperature_label = tk.Label(root, text="Temperature",
                                   font=('Arial', 20), bg='#EAE9EB', fg='#03045E')
    temperature_label.place(x=420, y=120)

    temperature_label2 = tk.Label(root, text="{}".format(info_dect["temperature"]),
                                   font=('Arial', 40), bg='#EAE9EB', fg='#fb8500')
    temperature_label2.place(x=470, y=160)

    wind_speed_label = tk.Label(root, text="Wind Speed \n {}".format(info_dect["wind_speed"]),
                                   font=('Arial', 20), bg='#EAE9EB', fg='#03045E')
    wind_speed_label.place(x=40, y=250)

    wind_direction_label = tk.Label(root, text="Wind Direction \n {}".format(info_dect["wind_direction"]),
                                   font=('Arial', 20), bg='#EAE9EB', fg='#03045E')
    wind_direction_label.place(x=300, y=250)

    weather_descriptions_label = tk.Label(root, text="Weather Descriptions \n {}".format(info_dect["weather_descriptions"]),
                                   font=('Arial', 20), bg='#EAE9EB', fg='#03045E')
    weather_descriptions_label.place(x=420, y=350)


    humidity_label = tk.Label(root, text="Humidity \n {}".format(info_dect["humidity"]),
                                   font=('Arial', 20), bg='#EAE9EB', fg='#03045E', width=10)
    humidity_label.place(x=580, y=250)

    feels_like_label = tk.Label(root, text="Feels Like \n {}".format(info_dect["feels_like"]),
                                   font=('Arial', 20), bg='#EAE9EB', fg='#03045E', width=10)
    feels_like_label.place(x=150, y=350)


def show_info():
    try:
        display_whaether_info(get_weather_info(country.get().strip()))
    except:
        messagebox.showerror("Country Error", "Please check the country name and try again")
    
def show_info_by_location():
    try:
        get_ip()
    except:
        messagebox.showerror("Error", "please Check your internet connection!")
    
    display_whaether_info(get_weather_info(get_ip))
    


weather_button = tk.Button(root, command=show_info, text=" Show Weather ", bg="#70A7D8", font=(20), fg="#042E56", activebackground="#70A7D8")
weather_button.place(x=70, y=110)

use_location_button = tk.Button(root,command=show_info_by_location,
                                 text="Use my location", bg="#70A7D8", font=(20), fg="#042E56", activebackground="#70A7D8")
use_location_button.place(x=70, y=150)



tk.mainloop()