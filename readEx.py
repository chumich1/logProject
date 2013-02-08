import re

f = open('log.txt', "r")
j = f.read()
d = re.findall(r'(?<=\<)(.*?)(?=\>)', j)
m = re.findall(r'(?<=\{)(.*?)(?=\})', j)
fe = re.findall(r'(?<=\[)(.*?)(?=\])', j)



for i in m: print i
f.close()



