#list is a data structure
myFam = ["mom", "dad", "sis","bro"]
print myFam
print myFam[0]          #to print an element in a given index
print myFam[1]          #0 gives 1st index, 1 gives 2nd....
print myFam [-1]        #-1 gives last index, -2 gives 2nd last....
myFam[1] = "granddad"       #mutating an element in the list
print myFam
print myFam[1]

print "--------------------------------------------------"

colours = ["red","white","orange"]
print colours
colours.append("purple")                        #adding another element to the end of the list
print colours
colours.insert(2,"green")                           #adding another element to a specific index to the list, everything after is shifted right
print colours
colours.remove("red")                               #searching the list and removing the first occurance of a specified piece of data
print colours
colours.sort()                                                  #rearranges list into alphabetical order (strings) or lowest to highest numbers (numbers)
print colours
colours.sort(reverse=True)                      #reverses list 
print colours

print "--------------------------------------------------"

myList = [[1,2],['6',6,6.0],True]
print myList[1]                                                 #when dealing with lists in lists, using one index gives you a whole list
print myList[1][0]                                          #to get a specific data
print myList[0][1]
print myList[2]

print "--------------------------------------------------"

print max( 71 , 3 , 53 , 10 )                                     #gives biggest number
print max(["a","t","c","g"])                                   #gives letter closest to "z"
print min (["a","t","c","g"])
print max("cat","dog", "zebra","giraffe")

print "--------------------------------------------------"

print "hello"
print len("hello")                                                   #to get length of a given object

print "--------------------------------------------------"
#every pass throuh a loop is an iteration
for x in range(10):
    print x,                                                                #using a comma prints then all on the same line
print ""

names =["matt" , "bob","Al", "Jon"]             #different ways to do lists and whatnot
for i in range(len(names)):
    print "hi", names[i]

myList = []
for x in range(5):
    myList.append(x)
print myList

print "--------------------------------------------------"

#Pyramid of golf balls
golfSum = 0
for x in range(26):
    golfSum+= x**2
print golfSum

print "--------------------------------------------------"

#structure of a compiunt statement is determined by:
#1) ()
#2) []
#3) {}

#Fibonacci Sequence
secondLast = 1
last = 1
print secondLast,
print last,

for index in range(15-2):
    current = secondLast + last
    print current,
    secondLast = last
    last = current
print ""

fib = [1,1]
for index in range(1,16):
    fib.append(fib[index-1]+fib[index])
print fib

print "--------------------------------------------------"

myString = "banananananana"
print myString.index("n")                               #just finds first n
print myString[:8]                                              #go to the 8th index (prings total 8 characters)
print myString[8:]                                              #print from 8 onwards

myList = list(myString)                               #turns the string into a list with individual characters
myList[0] = "p"
" ".join(myList)
print myList

print "--------------------------------------------------"

#MAJOR 1 PRACTICE
import math
R = input("input the radius of the circle (R)   ")
r = input("input the radius of the tube (r) ")

A = 4*(math.pi**2)*R*r
B = 4*(math.pi**2)*R*3*r
C = 100*abs((A-B)/B)
print "A = ", A
print "B = ",B
print "C = ", C

