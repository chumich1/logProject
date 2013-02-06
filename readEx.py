import re
p= re.compile(r'[<>]')
f = open('log.txt', "r")
print p.split(f.read())
f.close()
