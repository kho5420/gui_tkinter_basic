import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar.start(10)
# progressbar.pack()

# progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar2.start(10)
# progressbar2.pack()

# def btncmd():
#     progressbar.stop()

# btn = Button(root, text="클릭", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar3.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)

        p_var2.set(i)
        progressbar3.update()
        print(p_var2.get())

btn = Button(root, text="클릭", command=btncmd2)
btn.pack()

root.mainloop()