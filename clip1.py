from Tkinter import *
import pyperclip

mainlist = []
index=-1
copydict={}
root = Tk()


def Textwindow1(index):
     win=Toplevel()
##     canvas=Canvas(win)
##     canvas.pack(side=LEFT,fill=BOTH,expand=TRUE)
     frame1=Frame(win)
     sbar=Scrollbar(frame1)
     text1 = Text(frame1)
     text1.insert(INSERT,copydict[index])
     sbar.config(command=text1.yview)
     text1.config(yscrollcommand=sbar.set)
     sbar.pack(side=RIGHT,fill=Y,expand=False)
     text1.pack(side=LEFT,fill=BOTH,expand=True)
     frame1.pack()


def store():
    global root,index
    spam = pyperclip.paste()
    mainlist.append(spam)
    index=index+1
    copydict[index]=spam
    print(spam)
    frame_create = Frame(root, height=3, width=10)
    new_window=Button(frame_create, text="Expand",command=lambda: Textwindow1(index))
    text = Text(frame_create, height=5, width=100)
    text.insert(INSERT, spam[0:100])
    text.pack()
    new_window.pack(side=RIGHT)
    frame_create.pack()
    print(spam)


def get(index):
    item = mainlist[index]
    print item
    pyperclip.copy(item)


store_button = Button(root, text="store", command=store)
store_button.pack()
#root.pack(Tkinter.Tk.__init__(self))
root.mainloop()

