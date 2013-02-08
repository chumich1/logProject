a = "n"

while a.lower()!="y":
    x = raw_input("What would you like to do? (add, view)")

    if x.lower() == "add": execfile("add.py")
        

    elif x.lower() == "view": execfile("readEx.py")

    a = raw_input("are you done? (y/n)")

