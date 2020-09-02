import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("알림", "정상 예매")

def warn():
    msgbox.showwarning("경고", "매진되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류 발생")    

def okcancel():
    msgbox.askokcancel("확인/취소", "역방향입니다. 예매하시겠습니까?")    

def retrycancel():
    msgbox.askretrycancel("재시도/취소", "다시 시도?")

def yesno():
    msgbox.askyesno("예/아니오", "예/아니오")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="저장x")
    print("응답", response)    
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인/취소").pack()
Button(root, command=retrycancel, text="재시도/취소").pack()
Button(root, command=yesno, text="예/아니오").pack()
Button(root, command=yesnocancel, text="예/아니오/취소").pack()

root.mainloop()