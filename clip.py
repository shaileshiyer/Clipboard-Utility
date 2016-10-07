from tkinter import *
import pyperclip
mainlist=[]
root=Tk()


def store():
    global root
    spam=pyperclip.paste()
    mainlist.append(spam)
    frame_create= Frame(root,height=3 ,width=10)
    text= Text(frame_create,height=1,width=100)
    text.insert(INSERT,spam[0:100])
    text.pack(side=RIGHT)
    frame_create.pack()
    print(spam)
    
def get(index):
    item=mainlist[index]
    print item
    pyperclip.copy(item)

store_button=Button(root,text="store",command=store)
store_button.pack()





root.mainloop()                

