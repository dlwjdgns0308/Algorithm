from tkinter import *
import sqlite3

root = Tk()
root.title("수빈이의 전역일 계산기")
root.geometry("840x630+300+200")
image = PhotoImage(file="C:/Users/buol2/Desktop/gang.png")
wall = Label(image =image)
wall.place(x=0,y=0)


photo = PhotoImage(file="C:/Users/buol2/Desktop/시작버튼.png")

def btncmd():
    def confirm():
        in_text = input_text.get() 
        print(in_text)
    root.destroy()
    nroot = Tk()
    nroot.title("수빈이의 전역일 계산기")
    nroot.geometry("840x630+300+200")

    input_text = Entry(nroot, width=30)
    input_text.grid(column=0,row=2)

    button = Button(nroot, text="입력",command=confirm)
    button.grid(column=1,row=2)
btn1 = Button(root, image=photo, command=btncmd)
btn1.pack(side="bottom",pady=30)



root.resizable(False, False)
root.mainloop()