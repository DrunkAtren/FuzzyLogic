import customtkinter

customtkinter.set_appearance_mode("dark")

window = customtkinter.CTk()
#window.geometry("1920x1280")
window.geometry("400x460")
window.title("Fuzzy Logic")

frame = customtkinter.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill="both", expand=True)

def season_slider(value):
    print(value)
    lable_season.configure(text=f"Pora roku: {round(slider_season.get())}")
def time_slider(value):
    print(value)
    lable_time.configure(text=f"Godzina: {round(slider_time.get())}")
def room_temp_slider(value):
    print(value)
    lable_room_temp.configure(text=f"Temperatura Pokoju: {round(slider_room_temp.get())}")

#GIT
slider_season = customtkinter.CTkSlider(master=frame, command=season_slider, from_=1, to=4, number_of_steps=3)
slider_season.pack(pady=12, padx=10)
lable_season = customtkinter.CTkLabel(master=frame, text=f"Pora roku: {round(slider_season.get())}")
lable_season.pack(pady=12, padx=10)

slider_time = customtkinter.CTkSlider(master=frame, command=time_slider, from_=0, to=23, number_of_steps=23)
slider_time.pack(pady=12, padx=10)
lable_time = customtkinter.CTkLabel(master=frame, text=f"Godzina: {round(slider_time.get())}")
lable_time.pack(pady=12, padx=10)


slider_room_temp = customtkinter.CTkSlider(master=frame, command=room_temp_slider, from_=0, to =30, number_of_steps=30)
slider_room_temp.pack(pady=12, padx=10)
lable_room_temp = customtkinter.CTkLabel(master=frame, text=f"Temperatura Pokoju: {round(slider_room_temp.get())}")
lable_room_temp.pack(pady=12, padx=10)









window.mainloop()

# https://wanderlog.com/weather/9642/8/warsaw-weather-in-august
# Hours  [  1;  2;  3; 4;  5;   6;  7;  8;  9; 10; 11; 12; 13; 14; 15; 16; 17; 18; 19; 20; 21; 22; 23; 24;]

# Summer [ 18; 17; 16; 16; 15; 15; 15; 16; 18; 19; 20; 21; 22; 22; 22; 23; 23; 23; 22; 21; 21; 20; 19; 18;]
# Atum   [  7;  7;  7;  7;  6;  6;  6;  5;  6;  7;  8; 10; 11; 12; 12; 12; 12; 12; 11; 10; 10;  9;  8;  8;]
# Winter [ -4; -4; -4; -5; -5' -5; -5; -5; -5; -5; -5; -4; -3; -2; -2; -2; -2; -2; -3; -3; -3; -4; -4; -4;]
# Spring [  7;  7;  6;  6;  5;  5;  4;  5;  6;  8; 10; 11; 11; 12; 14; 14; 14; 14; 13; 12; 11; 10; 10;  9;]






