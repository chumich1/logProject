# menu-example-3.py

from Tkinter import *
from PIL import *


root = Tk()
root.title("Running Log 0.01")
background_image= PhotoImage(file="background2.gif")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
button = Button(root, text="HEY")
button.pack()

def hello():
    print "hello!"

def add():
    execfile("addGui.py")

def view():
    print "hey"

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

menubar.add_command(label="Add", command=add)
menubar.add_command(label="View", command=view)

# display the menu
root.config(menu=menubar)
root.mainloop()
 
