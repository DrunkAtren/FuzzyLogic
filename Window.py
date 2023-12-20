from tkinter import PhotoImage, Label, Canvas
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter
import numpy as np
import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("dark")
window = customtkinter.CTk()
window.geometry("1920x1280")

#window.geometry("400x460")
#window.geometry("1920x1280")
#window.geometry("1280x720")

window.title("Fuzzy Logic")
frame = customtkinter.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill="both", expand=True)

TEMP_OUTSIDE = np.array([
    [9, 7, 7, 6, 6, 5, 5, 4, 5, 6, 8, 10, 11, 11, 12, 14, 14, 14, 14, 13, 12, 11, 10, 10], #wiosna
    [18, 18, 17, 16, 16, 15, 15, 15, 16, 18, 19, 20, 21, 22, 22, 22, 23, 23, 23, 22, 21, 21, 20, 19], #lato
    [8, 7, 7, 7, 7, 6, 6, 6, 5, 6, 7, 8, 10, 11, 12, 12, 12, 12, 12, 11, 10, 10, 9,  8], #jesien
    [-4, -4, -4, -4, -5, -5, -5, -5, -5, -5, -5, -5, -4, -3, -2, -2, -2, -2, -2, -3, -3, -3, -4, -4], #zima
])
check_var = tk.IntVar()

TEMP = np.zeros((5, 120))
for i in range(0,120):
    x=i
    TEMP[0, i] = x

    #temperatura zimno
    if x >= -30 and x <= 5:
       zimno = 1
    elif x >= 5 and x <= 15:
       zimno = (15-x)/(15-5)
    else:
       zimno = 0
    TEMP[1,i] = zimno

    # temperatura letnio
    if x>=5 and x<=15:
       letnio=(x-5)/(15-5)
    elif x>=15 and x<=25:
       letnio=(25-x)/(25-15)
    else:
       letnio=0
    TEMP[2,i] = letnio

    # temperatura cieplo
    if x >= 15 and x <= 25:
        cieplo = (x - 15) / (25 - 15)
    elif x >= 25 and x <= 35:
        cieplo = (35 - x) / (35 - 25)
    else:
        cieplo = 0
    TEMP[3, i] = cieplo

    # temperatura bardzo goraca
    if x >= 25 and x <= 35:
        goraco = (x - 25) / (35 - 25)
    elif x >= 35 and x <= 40:
        goraco = 1
    else:
        goraco = 0
    TEMP[4, i] = goraco

UST = np.zeros((6, 110))
for i in range(0,110):
    x=i
    UST[0, i] = x

    if x == 0:
        UstWyl = 1
    else:
        UstWyl = 0
    UST[1, i] = UstWyl

    if x == 25:
        UstMaly = 1
    else:
        UstMaly = 0
    UST[2, i] = UstMaly

    if x == 50:
        UstSredni = 1
    else:
        UstSredni = 0
    UST[3, i] = UstSredni

    if x == 75:
        UstDuzy = 1
    else:
        UstDuzy = 0
    UST[4, i] = UstDuzy

    if x == 100:
        UstMax = 1
    else:
        UstMax = 0
    UST[5, i] = UstMax

def wykresy():
    plt.figure(1)

    plt.xlabel('Temperatura [C]')
    plt.ylabel('Wzrost')
    plt.title('Zbiór rozmyty temperatury')

    plt.plot(TEMP[0, :], TEMP[1, :], 'blue')
    plt.axis([0,40,0,1.1])

    plt.plot(TEMP[0, :], TEMP[2, :], 'green')
    plt.axis([0,40,0,1.1])

    plt.plot(TEMP[0, :], TEMP[3, :], 'orange')
    plt.axis([0,40,0,1.1])

    plt.plot(TEMP[0, :], TEMP[4, :], 'red')
    plt.axis([0,40,0,1.1])

    plt.figure(2)

    plt.title('Ust')

    plt.plot(UST[0, :], UST[1, :], 'b')
    plt.axis([0,100,0,1.1])

    plt.plot(UST[0, :], UST[2, :], 'b')
    plt.axis([0,100,0,1.1])

    plt.plot(UST[0, :], UST[3, :], 'b')
    plt.axis([0,100,0,1.1])

    plt.plot(UST[0, :], UST[4, :], 'b')
    plt.axis([0,100,0,1.1])

    plt.plot(UST[0, :], UST[5, :], 'b')
    plt.axis([0,100,0,1.1])

#Ustawienie
f = None
d = None
c = None
MocPiec = 1
TempPiec = 0
y = 0

#TempZew = -5
#TempUstawiana =30
#TempPokoju = TempZew + int(TempPiec / 10)
TempPokoju = 0
TEMP_TIME = np.zeros((2, 10000))
FIREPLACE_POWER = np.zeros((2, 10000))
TEMP_ROOM = np.zeros((2, 10000))
minutes = 0
inc = 0

frameCnt = 19
srcFlameGif = [PhotoImage(file='smoke.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]


def Tick():
    global MocPiec
    global y
    global Zmiana
    global TempPiec
    global TempPokoju
    global TempUstawiana

    season = int(slider_season.get()) - 1
    hour = int(slider_time.get())
    TempUstawiana = round(slider_fireplace_temp.get())
    TempZew = TEMP_OUTSIDE[season, hour]
    TempPokoju = TempZew + int(TempPiec / 10)

    if MocPiec==0:
        TempPokoju = TempPokoju - 2
    else:
        TempPokoju = TempPokoju + int(TempPiec / 15)


    Zmiana = TempUstawiana - TempPokoju

    print("-----")
    print(TempPiec, "Temperatura Pieca")

    print(TempPokoju,"Temperatura Pokoju")
    print(Zmiana, "Zmiana")
    print(TEMP[1, Zmiana], TEMP[2, Zmiana], TEMP[3, Zmiana], TEMP[4, Zmiana])

    R1 = TEMP[1, Zmiana]
    R2 = TEMP[2, Zmiana]
    R3 = TEMP[3, Zmiana]
    R4 = TEMP[4, Zmiana]
    R5 = 0 #else do regul


    wynik=(R5+R1+R2+R3+R4)
    if wynik>0:
        wynik=wynik
    elif wynik==0:
        wynik=1

    y = (R5*0+R1 * 25 + R2 * 50 + R3 * 75 + R4 * 100)/wynik
    print(y)

    # r1 IF Zmiana = Zimno THEN Maly
    # r2 IF Zmiana = Letnio  THEN Sredni
    # r3 IF Zmiana = Cieplo  THEN Duzy
    # r4 IF Zmiana = Goraco  THEN Max
    # r5 IF Zmiana<0 THEN Wylacz


    if y<=0 :
        MocPiec = 0
    elif y >= 100 :
        MocPiec = 5
    elif y >= 75:
        MocPiec = 4
    elif y >= 50:
        MocPiec = 3
    elif y >= 25:
        MocPiec = 2


    if MocPiec>0:
        TempPiec = TempPiec + MocPiec
    else:
        if TempPiec <= 0:
            TempPiec = 0
        else:
            TempPiec = TempPiec-2
    print(MocPiec)
def update_fire_texture():
    global TempPiec
    TEMP_FIREPLACE = TempPiec
    global srcFlameGif
    if TEMP_FIREPLACE < 5:
        srcFlameGif = [PhotoImage(file='smoke.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]
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
def update_fireplace():
    if check_var.get() == 1:
        global minutes
        global inc
        global TEMP_TIME
        global TEMP_ROOM
        global FIREPLACE_POWER
        global y
        global TempPokoju
        update_fire_texture()
        Tick()
        minutes = minutes +5
        inc = inc +1
        TEMP_TIME[0, inc] = minutes
        TEMP_TIME[1, inc] = TempPiec
        FIREPLACE_POWER[0, inc] = minutes
        FIREPLACE_POWER[1, inc] = y
        TEMP_ROOM[0, inc] = minutes
        TEMP_ROOM[1, inc] = TempPokoju
def update_graph_temp_room():
    c = plt.figure(6)
    v = c.add_subplot(111)
    v.set_title('Wykres wzrostu temperatury w pokoju w czasie')
    v.set_xlabel('Czas[5min]')
    v.set_ylabel('Temperatura[1C]')
    v.plot(TEMP_ROOM[0, :], TEMP_ROOM[1, :], 'blue')
    frm2 = tk.Frame(window)
    frm2.place(x=50, y=500)

    canvas3 = FigureCanvasTkAgg(c, master=frm2)
    canvas3.draw()
    canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
def update_graph_fire_power():
    d = plt.figure(4)
    b = d.add_subplot(111)
    b.set_title('Wykres wzrostu mocy w czasie')
    b.set_xlabel('Czas[5min]')
    b.set_ylabel('Moc Pieca')
    b.plot(FIREPLACE_POWER[0, :], FIREPLACE_POWER[1, :], 'blue')
    frm = tk.Frame(window)
    frm.place(x=1180, y=20)

    canvas = FigureCanvasTkAgg(d, master=frm)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def update_graph_temp_time():
    f = plt.figure(5)
    a = f.add_subplot(111)
    a.plot(TEMP_TIME[0, :], TEMP_TIME[1, :], 'blue')
    a.set_title('Wykres wzorstu temperatury pieca w czasie')
    a.set_xlabel('Czas[5min]')
    a.set_ylabel('Temperatura[1C]')
    frm1 = tk.Frame(window)
    frm1.place(x=1180, y=500)

    canvas1 = FigureCanvasTkAgg(f, master=frm1)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
def clear_graphs():
    global f
    global d
    global c
    f = plt.close()
    d = plt.close()
    c = plt.close()
def update_checkbox():
    clear_graphs()
    update_fireplace()
    update_graph_fire_power()
    update_graph_temp_time()
    update_graph_temp_room()
    window.after(5000, update_checkbox)
def update_outside_temperature():
    season = int(slider_season.get()) - 1
    hour = int(slider_time.get())
    label_outside_temp.configure(text=f"Temperatura na zewnątrz: {TEMP_OUTSIDE[season, hour]}")
def season_slider(value):
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
    label_fireplace_temp.configure(text=f"Docelowa temperatura Pokoju: {round(slider_fireplace_temp.get())}")


lbFlame = Label(window)
lbFlame.pack(pady=12, padx=10)
lbFlame.place(x=800, y=40)

slider_season = customtkinter.CTkSlider(master=frame, command=season_slider, from_=1, to=4, number_of_steps=3)
slider_season.pack(pady=12, padx=10)
slider_season.place(x=70, y=60)

slider_time = customtkinter.CTkSlider(master=frame, command=time_slider, from_=0, to=23, number_of_steps=23)
slider_time.pack(pady=12, padx=10)
slider_time.place(x=70, y=140)

slider_fireplace_temp = customtkinter.CTkSlider(master=frame, command=room_temp_slider, from_=0, to =30, number_of_steps=30)
slider_fireplace_temp.pack(pady=12, padx=10)
slider_fireplace_temp.place(x=70, y=230)

label_season = customtkinter.CTkLabel(master=frame, corner_radius=16, fg_color="black", text=f"Pora roku: Lato")
label_season.pack(pady=12, padx=10)
label_season.place(x=120, y=20)

label_time = customtkinter.CTkLabel(master=frame, corner_radius=16, fg_color="black", text=f"Godzina: {round(slider_time.get())}")
label_time.pack(pady=12, padx=10)
label_time.place(x=120, y=100)

label_outside_temp = customtkinter.CTkLabel(master=frame, corner_radius=16, fg_color="black", text=f"Temperatura na zewnątrz: 20")
label_outside_temp.pack(pady=12, padx=10)
label_outside_temp.place(x=800, y=400)

label_fireplace_temp = customtkinter.CTkLabel(master=frame, corner_radius=16, fg_color="black",
                                              text=f"Docelowa temperatura Pokoju: {round(slider_fireplace_temp.get())}")
label_fireplace_temp.pack(pady=12, padx=10)
label_fireplace_temp.place(x=70, y=180)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Włączenie Pieca:", command=update_checkbox, variable=check_var, onvalue=1, offvalue=0)
checkbox.pack(padx=20, pady=10)
checkbox.place(x=830, y=440)

window.after(0, update_fire_gif, 0)
window.mainloop()

# https://wanderlog.com/weather/9642/8/warsaw-weather-in-august