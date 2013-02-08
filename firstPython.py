a = "n"

while a.lower()!="y":
    x = raw_input("What would you like to do? (add, view, remove)")

    if x.lower() == "add": execfile("add.py")
        

    elif x.lower() == "view": execfile("readEx.py")

    elif x.lower() == "remove": execfile("remove.py")	

    a = raw_input("are you done? (y/n)")


