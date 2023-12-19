import Window
import piec

window = customtkinter.CTk()
#window.geometry("1920x1280")
window.geometry("1280x720")
#window.geometry("400x460")
window.title("Fuzzy Logic")



window.after(0, update_fire_gif, 0)
window.mainloop()
