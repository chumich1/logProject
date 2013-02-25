import re

f = open('log.txt', "r")
j = f.read()
d = re.findall(r'(?<=\<)(.*?)(?=\>)', j)
m = re.findall(r'(?<=\[)(.*?)(?=\])', j)
t = re.findall(r'(?<=\:_;)(.*?)(?=\;_:)', j)
fe = re.findall(r'(?<=\{)(.*?)(?=\})', j)



i = 0
while i<len(d): 
    print d[i], m[i], ": ", t[i], fe[i]
    i =i+1

f.close()
