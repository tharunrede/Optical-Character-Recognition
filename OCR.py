import pytesseract as tes
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile
import os 

tes.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
filename=''

top=tk.Tk(className=" OCR Using Tesseract")
top.geometry("300x300")

def closeWin():
    top.destroy()

def OCR(filename):
    try:
        img = Image.open(filename)
        t1 = tes.image_to_string(img)
        if t1 is None:
            pass
        else:
            return t1
    except Exception:
        pass

def getFileName():
    global filename
    file1 = askopenfile(mode ='r')
    if file1 is not None:
        filename=file1.name
    else:
         pass
    if (OCR(file1.name)) is None:
        pass
    else:
        display(OCR(file1.name),file1.name)

def display(str1,fname):
    try:
        if str1 != None:
            top1 = tk.Toplevel(top)
            l2=tk.Label(top1, text ="Provided Image")
            l3=tk.Label(top1, text ="OCR Result")
            img2 = Image.open(filename)
            height,width=img2.size
            img2 = img2.resize((height//2,width//2), Image.ANTIALIAS)
            img2 = ImageTk.PhotoImage(img2)
            panel = Label(top1, image=img2)
            panel.image = img2
            
            scroll = Scrollbar(top1)
            scroll.pack(side=RIGHT, fill=Y)
            t12=Text(top1,bd=2,padx=5,pady=5,wrap = WORD,yscrollcommand=scroll.set)
            t12.insert(INSERT, str1) 

            l2.pack()
            panel.pack()
            l3.pack()
            t12.pack()

            scroll.config(command=t12.yview)
        else: 
            pass     
    except Exception:
        pass

l1= tk.Label(top,text=" Choose an Image File")
l1.pack()
b1= tk.Button(top,text= 'Browse',command = getFileName,bd=3,padx=2,pady=2,relief=RIDGE).place(relx=0.5, rely=0.5,anchor= CENTER)
b2= tk.Button(top,text= 'Close',command = closeWin).place(x= 130,y=250)

top.mainloop()