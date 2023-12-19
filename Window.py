import _thread
import tkinter
from datetime import time
from tkinter import PhotoImage, Label, Canvas
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib import gridspec
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import customtkinter
import numpy as np
from PIL import Image, ImageSequence, ImageTk

customtkinter.set_appearance_mode("dark")

window = customtkinter.CTk()
#window.geometry("1920x1280")
window.geometry("1280x720")
#window.geometry("400x460")
window.title("Fuzzy Logic")

frame = customtkinter.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill="both", expand=True)



TEMP = np.array([
    [9, 7, 7, 6, 6, 5, 5, 4, 5, 6, 8, 10, 11, 11, 12, 14, 14, 14, 14, 13, 12, 11, 10, 10], #wiosna
    [18, 18, 17, 16, 16, 15, 15, 15, 16, 18, 19, 20, 21, 22, 22, 22, 23, 23, 23, 22, 21, 21, 20, 19], #lato
    [8, 7, 7, 7, 7, 6, 6, 6, 5, 6, 7, 8, 10, 11, 12, 12, 12, 12, 12, 11, 10, 10, 9,  8], #jesien
    [-4, -4, -4, -4, -5, -5, -5, -5, -5, -5, -5, -5, -4, -3, -2, -2, -2, -2, -2, -3, -3, -3, -4, -4], #zima
])

f = plt.figure(figsize=(4,24), dpi=100)
a = f.add_subplot(111)
a.plot([1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8])


frm = tk.Frame(window)
frm.place(x=600, y=50)

canvas = FigureCanvasTkAgg(f, master=frm)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


frameCnt = 19
srcFlameGif = [PhotoImage(file='smoke.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

def update_fire_texture():
    TEMP_FIREPLACE = int(slider_season.get())*3
    print(TEMP_FIREPLACE)
    global srcFlameGif
    if TEMP_FIREPLACE < 5:
        srcFlameGif = [PhotoImage(file='smoke.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]
        print("git")
    elif TEMP_FIREPLACE > 5 and TEMP_FIREPLACE <=10:
        srcFlameGif = [PhotoImage(file='ogien1.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]
    elif TEMP_FIREPLACE > 10 and TEMP_FIREPLACE <=15:
        srcFlameGif = [PhotoImage(file='ogien2.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]
    elif TEMP_FIREPLACE >15 and TEMP_FIREPLACE <=20:
        srcFlameGif = [PhotoImage(file='ogien3.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]
    elif TEMP_FIREPLACE >20 and TEMP_FIREPLACE <=25:
        srcFlameGif = [PhotoImage(file='ogien4.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]
    elif (TEMP_FIREPLACE >25) and (TEMP_FIREPLACE <=30):
        srcFlameGif = [PhotoImage(file='ogien5.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]
    else:
        print("Blad")
def update_fire_gif(ind):
    imgFlame = srcFlameGif[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    lbFlame.configure(image=imgFlame, bg='black')
    window.after(150, update_fire_gif, ind)
def update_outside_temperature():
    season = int(slider_season.get()) - 1
    hour = int(slider_time.get())
    label_outside_temp.configure(text=f"Temperatura na zewnątrz: {TEMP[season, hour]}")
def season_slider(value):
    update_fire_texture()
    season = slider_season.get()
    match season:
        case 1:
            label_season.configure(text=f"Pora roku: Wiosna")
        case 2:
            label_season.configure(text=f"Pora roku: Lato")
        case 3:
            label_season.configure(text=f"Pora roku: Jesień")
        case 4:
            label_season.configure(text=f"Pora roku: Zima")
        case _:
            label_season.configure(text=f"Pora roku: Błąd zła pora roku")
    #lable_season.configure(text=f"Pora roku: {round(slider_season.get())}")
    update_outside_temperature()
def time_slider(value):
    label_time.configure(text=f"Godzina: {round(slider_time.get())}")
    update_outside_temperature()
def room_temp_slider(value):
    label_fireplace_temp.configure(text=f"Docelowa temperatura Pieca: {round(slider_fireplace_temp.get())}")

lbFlame = Label(window)
lbFlame.pack(pady=12, padx=10)
lbFlame.place(x=70, y=30)


slider_season = customtkinter.CTkSlider(master=frame, command=season_slider, from_=1, to=4, number_of_steps=3)
slider_season.pack(pady=12, padx=10)
slider_season.place(x=70, y=420)

slider_time = customtkinter.CTkSlider(master=frame, command=time_slider, from_=0, to=23, number_of_steps=23)
slider_time.pack(pady=12, padx=10)
slider_time.place(x=70, y=490)


label_season = customtkinter.CTkLabel(master=frame, corner_radius=16, fg_color="black", text=f"Pora roku: Lato")
label_season.pack(pady=12, padx=10)
label_season.place(x=120, y=380)

label_time = customtkinter.CTkLabel(master=frame, corner_radius=16, fg_color="black", text=f"Godzina: {round(slider_time.get())}")
label_time.pack(pady=12, padx=10)
label_time.place(x=120, y=450)

label_outside_temp = customtkinter.CTkLabel(master=frame, corner_radius=16, fg_color="black", text=f"Temperatura na zewnątrz: 20")
label_outside_temp.pack(pady=12, padx=10)
label_outside_temp.place(x=75, y=520)

slider_fireplace_temp = customtkinter.CTkSlider(master=frame, command=room_temp_slider, from_=0, to =30, number_of_steps=30)
slider_fireplace_temp.pack(pady=12, padx=10)
label_fireplace_temp = customtkinter.CTkLabel(master=frame, text=f"Docelowa temperatura Pieca: {round(slider_fireplace_temp.get())}")
label_fireplace_temp.pack(pady=12, padx=10)






window.after(0, update_fire_gif, 0)
window.mainloop()

# https://wanderlog.com/weather/9642/8/warsaw-weather-in-august





