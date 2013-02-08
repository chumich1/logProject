date = raw_input("What was the date of this run? (mm/dd/yyyy) ")
numberOfRuns = raw_input("How many times did you run today? (enter an integer) ")

count = 0
total = 0
tempNum = 0
miles = []
while count < int(numberOfRuns):
    tempNum = input("How many miles for run "+ str(count+1)+ "? ")
    total = total + tempNum
    miles.insert(count, tempNum)
    count = count +1
    
feel = raw_input("How did you feel? ")


f = open('log.txt','a')
f.write("<"+date+">"+str(miles)+"{"+feel+"}"+":_:"+str(total)+":_:")

f.close()



