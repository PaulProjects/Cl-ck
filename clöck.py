from cProfile import label
from datetime import datetime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Clöck')

label = Label(root,font = ('aerial',60), background='black', foreground='white')
def time():
    label.config(text=datetime.now().strftime("%F\n%H:%M:%S.%f"))
    label.after(1, time)

label.pack(anchor='center')
time()

mainloop()
