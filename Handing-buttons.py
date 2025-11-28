# step1: import tkinter
from  tkinter import *

# step2: gui interaction
window = Tk()

# step3: adding inputs
window.title("Adarsh")  
window.geometry("500x500")
def _log_entry():
    print("Button clicked!")
button = Button(window, text="Click Me", command=_log_entry, bg="lightgreen", fg="black", font=("Arial", 14),activebackground="lightblue", activeforeground="black")
button.pack()

# step4: mainloop
window.mainloop()