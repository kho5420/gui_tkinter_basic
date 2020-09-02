from tkinter import *

root = Tk()
root.title("GUI")

label1 = Label(root, text="하이")
label1.pack()

photo = PhotoImage(file="img2.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="바이")

    photo2 = PhotoImage(file="img2.png")
    label2.config(imgae=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.geometry("640x480")
# root.geometry("640x480+300+300") # 가로/세로/X좌표/y좌표

root.resizable(False, False) # 창 크기 변경 비활성

root.mainloop()