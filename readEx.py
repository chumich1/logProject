import re

f = open('log.txt', "r")
j = f.read()
d = re.findall(r'(?<=\<)(.*?)(?=\>)', j)
m = re.findall(r'(?<=\{)(.*?)(?=\})', j)
fe = re.findall(r'(?<=\[)(.*?)(?=\])', j)

i = 0
while i<len(d): 
    print d[i], m[i], fe[i]
    i =i+1

f.close()
