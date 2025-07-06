from tkinter import *
from datetime import date

root=Tk()
root.title("Getting starting with Widgets")
root.geometry("400x300")

lbl=Label(text="Hey There!",fg="white",bg="#072F5F",height=1,width=300)

name_lbl=Label(text="Full Name",bg="#3895D3")
name_entry=Entry()

def display():
    name=name_entry.get()
    global Message
    Message="Welcome to the Aplication!\nToday's date is:"
    greet="Hello "+name+"\n"

    text_box.insert(END,greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())

text_box=Text(height=3)
btn=Button(text="Begin",command=display,height=1,bg="#1261A0",fg="white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
mainloop()