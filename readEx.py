import re

f = open('log.txt', "r")
j = f.read()
d = re.findall(r'(?<=\<)(.*?)(?=\>)', j)
m = re.findall(r'(?<=\{)(.*?)(?=\})', j)
fe = re.findall(r'(?<=\[)(.*?)(?=\])', j)


print d[1], m[1], fe[1]
print "\n", int(m[0])+int(m[1])
f.close()
