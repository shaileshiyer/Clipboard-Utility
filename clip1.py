from tkinter import *
import pyperclip

mainlist = []
index=-1
copydict={}
root = Tk()

def new_window1(index):
     win=Toplevel()
     #sbar=Scrollbar(win,orient=VERTICAL)
     #sbar.pack(side=RIGHT,fill=Y,expand=FALSE)
     #canvas=Canvas(win,yscrollcommand=sbar.set)
     #canvas.pack(side=LEFT,fill=BOTH,expand=TRUE)

     frame1=Frame(win)
     text1 = Text(frame1)
     text1.insert(INSERT,copydict[index])
     text1.pack()
     frame1.pack()


def store():
    global root,index


    spam = pyperclip.paste()
    mainlist.append(spam)
    index=index+1
    copydict[index]=spam
    print(spam)
    frame_create = Frame(root, height=3, width=10)
    new_window=Button(frame_create, text="Expand",command=lambda: new_window1(index))
    text = Text(frame_create, height=5, width=100)
    text.insert(INSERT, spam[0:100])
    text.pack()
    new_window.pack(side=RIGHT)
    frame_create.pack()
    print(spam)


def get(index):
    item = mainlist[index]
    print
    item
    pyperclip.copy(item)


store_button = Button(root, text="store", command=store)
store_button.pack()
root.pack(bg=YELLOW)
root.mainloop()

