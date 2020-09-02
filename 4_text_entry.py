from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자 입력")

e = Entry(root, width=30) # 한줄로
e.pack()
e.insert(0, "한줄만 입력")

def btncmd():
    print(txt.get("1.0", END)) # 1:첫번쨰라인, 0:0번째 column위치
    print(e.get())

    #삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()