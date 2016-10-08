from tkinter import *
import pyperclip

mainlist = []
buttonlist=[]
buttonlist1=[]

index=-1
copydict={}
root = Tk()

def new_window1(message):

     win=Toplevel()
     frame1=Frame(win)
     sbar=Scrollbar(frame1)
     text1 = Text(frame1)
     text1.insert(INSERT,message)
     sbar.config(command=text1.yview)
     text1.config(yscrollcommand=sbar.set)
     sbar.pack(side=RIGHT,fill=Y,expand=False)
     text1.pack(side=LEFT,fill=BOTH,expand=True)
     frame1.pack()

def copy1(message):
    pyperclip.copy(message)


def store():
    global root,index
    spam = pyperclip.paste()
    mainlist.append(spam)
    index=index+1

    copydict[index]=spam
    print(copydict)
    frame_create = Frame(root, height=3, width=10)
    new_window=Button(frame_create, text="Expand",command=lambda : new_window1(spam))
    copy_button=Button(frame_create,text="Copy",command=lambda : copy1(spam))
    buttonlist.append(new_window)
    buttonlist1.append(copy_button)
    print(buttonlist)
    text = Text(frame_create, height=5, width=100)
    text.insert(INSERT, spam[0:100])
    text.pack()
    buttonlist[index].pack()
    buttonlist1[index].pack()
    #print(buttonlist.index(new_window))
    frame_create.pack()
    print(spam)


def get(index):
    item = mainlist[index]
    print
    item
    pyperclip.copy(item)


store_button = Button(root, text="store", command=store)
store_button.pack()

root.mainloop()

