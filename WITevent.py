from tkinter import * 

def convert():
    inch=float(entry.get())
    cm=inch * 2.54
    result["text"]= str (cm) + "inch"

root=Tk()
root.title("Inch to CM converter")
root.geometry("250x150")

entry=Entry(root)
entry.pack(pady=10)

Button(root,text="convert",command=convert).pack()

result=Label(root,text="")
result.pack(pady=10)

root. mainloop()