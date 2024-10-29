import time
import os
import tkinter.messagebox
from tkinter import *
l =Tk(className="Clock")
l.iconname("clock")
p1 = PhotoImage(file = 'img/digital-clock.png')
light = PhotoImage(file="img/sun(1).png")
dark = PhotoImage(file="img/sun(3).png") 
switch_value = True
l.iconphoto(False, p1)
l.title(">------Clock------>")
l.config(bg="#9381FF")
Lbel = Label(l, font=("BLUE CHERIES", 150), background="#9381FF", fg="#190B28")
def clock():
  clck = time.strftime("%H:%M:%S %P")
  Lbel.config(text=clck)
  Lbel.after(100, clock)
def toggle():
  
    global switch_value
    if switch_value == True:
        switch.config(image=dark, bg="#190B28",
                      activebackground="#190B28")
        Lbel.config(background="#190B28", fg="#9381FF")
        l.config(bg="#190B28")  
        switch_value = False
  
    else:
        switch.config(image=light, bg="#9381FF", 
                      activebackground="#9381FF")
        Lbel.config(background="#9381FF", fg="#190B28")
        l.config(bg="#9381FF")  
        switch_value = True
switch = Button(l, image=light,
                bd=0, bg="#9381FF",
                activebackground="#9381FF", 
                command=toggle)
switch.place(x=0,y=0)
Lbel.pack(pady=300,padx=100)
clock()
mainloop()
