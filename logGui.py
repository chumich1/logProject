# menu-example-3.py

from Tkinter import *



root = Tk()

top = Frame(width=500, height=500)
viewFrame = Frame(width=600, height=600)
def hello():
    print "hello!"

def add():
    viewFrame.destroy()
    top = Frame(width=500, height=500)
    top.pack()
    addText = Text(top, width=30, height=15)
    addText.pack()

def view():
    viewFrame = Frame(width=600, height=600)
    top.destroy() 
    viewFrame.pack()

menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

menubar.add_command(label="Add", command=add)
menubar.add_command(label="View", command=view)

# display the menu
root.config(menu=menubar)
mainloop()
