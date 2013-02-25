import re

f = open('log.txt', "r")
j = f.read()
d = re.findall(r'(?<=\<)(.*?)(?=\>)', j)
m = re.findall(r'(?<=\[)(.*?)(?=\])', j)
t = re.findall(r'(?<=\:_;)(.*?)(?=\;_:)', j)
fe = re.findall(r'(?<=\{)(.*?)(?=\})', j)
f.close()
print "Which would you like to remove? (enter 0 for none)"

i = 0
while i<len(d): 
    print  i+1, d[i], m[i], ": ", t[i], fe[i]
    i =i+1

x = input("Workout #: ")
if x != 0:

    del d[x-1]
    del m[x-1]
    del t[x-1]
    del fe[x-1]




    f = open('log.txt','w')

    i = 0
    while i<len(d):
        f.write("<"+d[i]+">"+"["+m[i]+"]"+"{"+fe[i]+"}"+":_;"+t[i]+";_:") 
        i =i+1

    f.close()


