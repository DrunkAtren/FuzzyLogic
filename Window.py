import customtkinter

customtkinter.set_appearance_mode("dark")

window = customtkinter.CTk()
window.geometry("1920x1280")

frame = customtkinter.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill="both", expand=True)
def slider_time(value):
    print(value)

slider_time = customtkinter.CTkSlider(master=frame, command=slider_time, from_ = 0, to = 24, number_of_steps=24)
slider_time.pack(pady=12, padx=10)
slider_time.set(0.5)




window.mainloop()

# https://wanderlog.com/weather/9642/8/warsaw-weather-in-august
# Hours  [  1;  2;  3; 4;  5;   6;  7;  8;  9; 10; 11; 12; 13; 14; 15; 16; 17; 18; 19; 20; 21; 22; 23; 24;]

# Summer [ 18; 17; 16; 16; 15; 15; 15; 16; 18; 19; 20; 21; 22; 22; 22; 23; 23; 23; 22; 21; 21; 20; 19; 18;]
# Atum   [  7;  7;  7;  7;  6;  6;  6;  5;  6;  7;  8; 10; 11; 12; 12; 12; 12; 12; 11; 10; 10;  9;  8;  8;]
# Winter [ -4; -4; -4; -5; -5' -5; -5; -5; -5; -5; -5; -4; -3; -2; -2; -2; -2; -2; -3; -3; -3; -4; -4; -4;]
# Spring [  7;  7;  6;  6;  5;  5;  4;  5;  6;  8; 10; 11; 11; 12; 14; 14; 14; 14; 13; 12; 11; 10; 10;  9;]






