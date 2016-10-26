##this project is created by Shailesh V Iyer ,Uday Menon and Nandukumar Mudaliar.
##the librarys used are tkinter for GUI and pyperclip to access the pastebuffer and interact with it.
from tkinter import *
import pyperclip

##mainlist = []
buttonlist = []
buttonlist1 = []

##index=-1
##copydict is the main dictionary
copydict={}
root = Tk()


class staticindex:
    ##this class here is responsible for maintaining unique indexes for each item
    index = 0


indexinstance = staticindex()


def textwindow1(indexer):
    ##this function is used for looking at the complete text in another window with a scrollbar
    print(indexer)
    win = Toplevel()
    frame1 = Frame(win)
    sbar = Scrollbar(frame1)
    text1 = Text(frame1)
    text1.insert(INSERT, copydict[indexer])
    sbar.config(command=text1.yview)
    text1.config(yscrollcommand=sbar.set)
    sbar.pack(side=RIGHT, fill=Y, expand=False)
    text1.pack(side=LEFT, fill=BOTH, expand=True)
    frame1.pack()


def store():
    ##this function is used to store copy contents into a dictionary and get the respective frame for content
    global root, indexinstance
    spam = pyperclip.paste()

    currentindex = indexinstance.index

    copydict[currentindex] = spam


    frame_create = Frame(root, height=3, width=10)
    new_window = Button(frame_create, text="Expand", command=lambda: textwindow1(currentindex))
    copy_button = Button(frame_create, text="Copy", command=lambda: get(currentindex))
    remove_button= Button(frame_create,text="remove",command=lambda:remove(currentindex,frame_create))
    buttonlist.append(new_window)
    buttonlist1.append(copy_button)

    print(buttonlist)
    text = Text(frame_create, height=5, width=100)
    text.insert(INSERT, spam[0:100])
    text.pack()
    buttonlist[currentindex].pack()
    buttonlist1[currentindex].pack()
    remove_button.pack()

    frame_create.pack()
    print(spam)
    indexinstance.index += 1


def get(index):
    ##this is used to copy a text into the paste buffer
    print (index)
    item = copydict[index]
    print (item)
    pyperclip.copy(item)

def remove(index,frame):
    ##this is used to remove an item and its respective frame
    copydict.pop(index)
    frame.destroy()
    print(copydict)
    print (index)

##this is the main function which runs  the GUI main loop and contains the store button

store_button = Button(root, text="store", command=store)
store_button.pack()

root.mainloop()