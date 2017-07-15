import random

print random.random()                 #random number from 0-1
print random.randint(0,100)         #random number from a,b inclusive
print random.randrange (10,200,10)      #random integer from a,b with steps
print random.choice('this is a string')     #random point in sequence

print "--------------------------------------"

outFile = open("tutorial example.txt", 'w')         #w = write
outFile.write("Hello World")                                    #write a line to the file
outFile.write("Hello World")
outFile.write("Hello World")                                    #all prints out in one line
outFile.close()                                                             #don't forget to close!

print "--------------------------------------"

inFile = open("tutorial example.txt" , "r")        #open file
contents = inFile.read()                                        #entire file as single string
print contents
inFile.close()
#help(file) whenever you need to know something/forgot something

print "--------------------------------------"

outFile = open("grades.txt", "w")
for i in range(800):
    #x = random.randint(0,12)
    x = int(random.gauss(7,3))                   #gaussian distribution
    x = max(min(x,12),0)                            #prevents negative and numbers above 12
    outFile.write(str(x) + "\n")
outFile.close()

grades = [0]*13
inFile = open("grades.txt","r")
for line in inFile:
    index = int(line)
    grades[index] = grades[index]+1
print grades
inFile.close()

##fig = pylab.figure()
##ax = fog.add_subplot(1,1,1)
##x = range(13)
##y = grades
##ax.bar(x,y)
##pylab.show()

print "--------------------------------------"

#MIDTERM MATERIAL
import graphics                 #graphics window is 200x200 pixels, origin is top left and goes down to bottom right as x,y ++
#myWindow = graphics.GraphWin("a line")
a = graphics.Point(20,30)
b = graphics.Point(180,170)
myLine = graphics.Line(a,b)
#myLine.draw(myWindow)

#myPoint = myWindow.getMouse()
#print myPoint

#DRAWINGS ARE OBJECTS, CANNOT SET X = Y, THEY HAVE SAME POINTER

print "--------------------------------------"

import string
outFile = open("ml2.txt", "w")
for i in range(50):
    outFile.write(str(random.randint(1,10)) + ",")
outFile.close()

inFile = open("ml2.txt", "r")
theList = inFile.read()
splitList = string.split(theList,',')
print splitList

abSum = 0
bSum = 0
for x in range(0,len(splitList)-1, 2):
    abSum += int(splitList[x]) *  int(splitList[x+1])
    print abSum
    bSum +=  int(splitList[x+1])
    print bSum

print abSum/float(bSum)


