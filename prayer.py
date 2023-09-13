import tkinter as tk
from tkinter import ttk, messagebox
import requests
app = tk.Tk()
app.title("Prayer Time")

def fetch_time(city, cuntry):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={cuntry}&method=5"
    try:
        response = requests.get(url)
        info = response.json()
        if "data" in info:
            timings = info["data"]["timings"]
            return timings
        else:
            return None
    except Exception as e:
        return f"unexpected error occured{e}"

def gui_fetch_prayer_time():
    city = city_entry.get()
    country = country_entry.get()
    if city and country:
        prayer_times = fetch_time(city , country)
        for name , time in prayer_times.items():
            results.insert(tk.END , f'{name}:    {time}')
    else:
        messagebox.showerror('Error' ,"unable to fetch prayer times, please enter correct city and country names")

frame = ttk.Frame(app , padding="20")
frame.grid(row=0, column=0)

city_label = ttk.Label(frame, text="City: ")
city_label.grid(row=0, column=0, pady=8)
city_entry = ttk.Entry(frame, width=30)
city_entry.grid(row=0, column=1, pady=8)

country_label = ttk.Label(frame, text="Country: ")
country_label.grid(row=1, column=0, pady=8)
country_entry = ttk.Entry(frame, width=30)
country_entry.grid(row=1, column=1, pady=8)

fetch_button = ttk.Button(frame, text="Get prayer time" , command=gui_fetch_prayer_time)
fetch_button.grid(row=2 , column=0, columnspan=4, pady=8)

results = tk.Listbox(frame, height=11 ,width=40)
results.grid(row=3 , column=0 , columnspan=2 , pady=8 )

tk.mainloop()