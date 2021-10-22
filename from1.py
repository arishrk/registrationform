from tkinter import *
from tkinter import ttk
window = Tk()
window.title("welcome to our page")
window.geometry("500x400")
window.configure(background = "blue")
ttk.Button(window,text="hello,arish").grid()
window.mainloop()