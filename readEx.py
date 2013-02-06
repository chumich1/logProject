import re
f = open('log.txt', "r")
fe= re.compile(r"(?<=\[)(.*?)(?=\])")
feels = fe.findall(f.read())
d = re.compile(r"(?<=<)(.*?)(?=>)")
date = d.findall(f.read())
m= re.compile(r"(?<=\{)(.*?)(?=\})")
miles = m.findall(f.read())





print date, miles, feels

f.close()
