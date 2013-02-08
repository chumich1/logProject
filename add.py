

date = raw_input("What was the date of this run? (mm/dd/yyyy) ")
miles = input("How many miles? ")
feel = raw_input("How did you feel? ")


f = open('log.txt','a')
f.write("<"+date+">"+"{"+str(miles)+"}"+"["+feel+"]")

f.close()




