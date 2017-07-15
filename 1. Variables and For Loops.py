import sys
import math

#temp = x 
#x = y
#y = temp       (normal way to swap two values)

#x,y = y,x        (Python way to swap two values)

print sys.maxint                          #highest integer number (32bit)
print type(sys.maxint)              #max 32 bits
print type(sys.maxint+1)         #after 32 bits it becomes a long type

print ("---------------------------------------------")

myStr = "spam"
print myStr
print 3*myStr
#print 3.0*myStr        (Will not work, cannot multiply a string type by a float)
print list(myStr)

print ("---------------------------------------------")

myInt = 5
print myInt
myInt = float(myInt)
print myInt

abs(-7)             #Prints out absolute value of -7 which is 7
round (1.6)     #Rounds 1.6 to 2

myInt = 1.6
print myInt
myInt = int(myInt)      #chops off the decimal instead of rounding (truncating)
print myInt

print ("---------------------------------------------")

spam2 = 42
print "hello my number is spam2"
#print "hello my number is" + spam2                      Cannot work with two different types at once (string and int)
print "hello my number is " + str(spam2)                #Converts the integer spam2 into a string type

print ("---------------------------------------------")

myInt = 25
print myInt
print math.sqrt(myInt)              #also returns value as a float so that functions return consistant data types (like root of 8)
from math import *
print sqrt(myInt)                           #shorter and lazier way that avoids the dot notation (must use the [from math import *])
                                                             #possible to run into errors when using this when multiple libraries share the same function name
print math.pi
print math.sin (math.pi/2)          #always in radians
print math.sin(math.pi)               #doesn't give 0 due to some float number approximation
print math.cos(math.pi)

print ("---------------------------------------------")

#REMEMBER TO READ SIGMA NOTATIONS FOR MAJOR LAB
#When doing sigma notation with a higher starting number than the ending number, answer is 0
#When doing product notation with a higher starting number than the ending number, answer is 1


for i in range(4):                  #don't forget the colon (:) and number in the brackets = number of repetitions
    print 4                                 #a range of 4 will go from 0,1,2,3
print range(4)
print range (1,6)                #range of 1,6 will go from 1,2,3,4,5
print range (-2, 10, 2)      #3rd parameter is a step (count by 2)
#note: cannot count backwards, range can only go forwards

print ("---------------------------------------------")

#summation example 1+2+3+4+5
accum = 0                            
for i in range(6):                #0,1,2,3,4,5 (no 6)
    accum+= i
    print accum

print ("---------------------------------------------")

#product notation example 1*2*3*4*5
accum=1
for i in range(1,6):
    accum = accum*i
    print accum

print ("---------------------------------------------")

#capa trig question on tutorial slides
sideA = 5.44
sideB = 5.44
sideC = 7.8
#c^2 = a^2 + b^2 - 2abcosC

angle = math.acos((sideC**2 - sideA**2 - sideB**2)/(-2*sideA*sideB))
print angle
