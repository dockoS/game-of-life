import tkinter
from time import time, sleep




root = tkinter.Tk()
root.geometry("800x600")

canvas = tkinter.Canvas(root)
counter = tkinter.IntVar()
counter.set(0)
canvas.pack()
counterObj = canvas.create_text((25,20), text=counter.get(),fill="red")

def UpdateFunction():
    counter.set(counter.get() + 1)
    canvas.itemconfig(counterObj,text=counter.get())
    print(counter.get())
    root.after(1000,UpdateFunction)
    
    
#sleep(1)
#canvas.create_text((40, 100), text=counter.get())

root.after(1000,UpdateFunction)
    
root.mainloop()