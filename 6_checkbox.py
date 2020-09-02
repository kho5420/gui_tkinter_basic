from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

checkvar = IntVar() #checkbar에 int형으로 값저장
checkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=checkvar)
#체크박스 선택/해제
# checkbox.select()
# checkbox.deselect()
checkbox.pack()

checkvar2 = IntVar()
checkbox2 = Checkbutton(root, text="일주일간 보지 않기", variable=checkvar2)
checkbox2.pack()

def btncmd():
    print(checkvar.get())
    print(checkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()